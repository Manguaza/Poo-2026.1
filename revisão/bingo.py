import random

class bingo: 
    def__int__(self, num_bolas):
    self.__num_bolas = num_bolas
    self.bolas = []
    def proximo (self):
        if len (self._bolas) == self._num bolas:
        return -1
    x = random.randint (1, self.__num_bolas)
    while x in self.__bolas:
        x - random.randint(1, self.__num bolas)
        self.__bolas.append(x)
        return x
    def sorteados (self):
        return self.__bolas
    b = bingo (10)
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
    print(b.proximo())
