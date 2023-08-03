# 这个文件的目标是创建一类纸牌对象
import collections
import random
lis1 = [i for i in 'Spade Heart Diamond Club'.split()]
lis2 = [str(j) for j in range(2, 11)] + list("JQKA")
Card = collections.namedtuple("Card", ("col", "num"))
class Cardesk:
   def __init__(self):
        self.Cards = [Card(x, y) for x in lis1 for y in lis2]

   def __getitem__(self, position):
       return self.Cards[position]

   def __len__(self):
       return len(self.Cards)

   def random(self):
       if 1 < self.__len__():
           tem1 = random.randint(0, self.__len__()-1)
           card1 = self.Cards[tem1]
           del self.Cards[tem1]
           return card1
       else:
           return

def distribute(Card, box, n):
    for i in range(n):
        box.append(Card.random())
    return

a = 0