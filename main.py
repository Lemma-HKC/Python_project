# 这是21点程序的主逻辑
# 导入其他模块并输出欢迎语句
from Card import *
def main():
    # namecheck = int(input(
    # '''
    # Welcome to the 21Point！
    # if you want to be a framehouse, enter 1 please;
    # if player, enter 2;
    # '''
    # ))
    # num_p = int(input(
    # '''
    # Input the number of entire people(between 2 and 6):
    # '''
    # ))
    num_p = 6
    # 生成初始扑克牌
    poker1 = Cardesk()
    # 生成玩家牌库
    p_box = [[] for i in range(num_p)]
    p_score = [[0] for j in range(num_p)]
    # 生成庄家牌库
    f_box = []
    f_score = 0
    # 进入开局流程，依次给玩家发两张牌
    for i in range(num_p):
        distribute(poker1, p_box[i-1], 2)

    # 构造加分函数
    def add_score(item):
        score = 0
        if item.num in "JQKA":
            if item.num in "A":
                score += 11
            else:
                score += 10
        else:
            score += int(item.num)
        return score

    # 检查花牌数量
    for i in range(num_p):
        tp = p_box[i-1]
        for item in tp:
            p_score[i-1][0] += add_score(item)

    BJ_list = []
    for i in range(num_p):
        if sum(p_score[i-1]) == 21:
            #print(f"we find Black-Jcak, Player{i} has the BJ")
            BJ_list.append(i)
        else:
            continue

    # 发牌给庄家
    distribute(poker1, f_box, 2)

    # 为庄家记分
    for item in f_box:
        f_score += add_score(item)

    #print("framehouse show ", f_box[0])

    # 初始环节结束，非黑杰克玩家们开始根据策略拿牌
    out_players = []
    for i in range(num_p):
        # 判断该玩家是否BJ
        catch = True
        while catch:
            inipoint = sum(p_score[i])
            if inipoint <= 11:
                distribute(poker1, p_box[i], 1)
                p_score[i][0] += add_score(p_box[i][-1])

            elif 11 < inipoint < 19:
                hit_prob = 0.6
                if random.random() <= hit_prob:
                    distribute(poker1, p_box[i], 1)
                    p_score[i][0] += add_score(p_box[i][-1])
                else:
                    #print(f"Player{i + 1} stand! total point is {inipoint}")
                    catch = False
            elif inipoint == 19:
                hit_prob = 1/13
                if random.random() <= hit_prob:
                    distribute(poker1, p_box[i], 1)
                    p_score[i][0] += add_score(p_box[i][-1])
                else:
                    #print(f"Player{i + 1} stand! total point is {inipoint}")
                    catch = False
                    continue
            elif 20 <= inipoint <= 21:
                    #print(f"Player{i + 1} stand! total point is {inipoint}")
                    catch = False
                    continue
            elif inipoint > 21:
                #print(f"Player{i} out with {inipoint} points!")
                out_players.append(inipoint)
                catch = False
                continue
    #print(p_score)
    #print(f"framehouse show his point :{f_score}")

    f_catch = True
    winORlose = 0
    sett = [sum(x) for x in p_score if sum(x) <= 21]
    while f_catch:
        if f_score < 17:
            distribute(poker1, f_box, 1)
            f_score += add_score(f_box[-1])
        elif f_score >= 17:
            if sett:
                if f_score < max(sett) and f_score < 21:
                    distribute(poker1, f_box, 1)
                    distribute(poker1, f_box, 1)
                    f_score += add_score(f_box[-1])
                    f_catch = False
                elif f_score == 21:
                    #print(f"framehouse stop the game with {f_score} Points")
                    f_catch = False
                elif f_score > 21:
                    #print(f"framehouse lose the game with {f_score} Points")
                    winORlose = 0
                    f_catch = False
                else:
                    #print(f"framehouse stop the game with {f_score} Points")
                    f_catch = False
            else:
                winORlose = 1
                f_catch = False

    if sett:
        winORlose = 1 if f_score >= max([sum(x) for x in p_score if sum(x) <= 21]) \
            else 0
        yield winORlose
    else:
        yield 1

wins = 0
board = sum(next(main()) for i in range(int(input("numbers of game:"))))

print(f"total winning game as framehouse is {board}")