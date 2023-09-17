from random import randint as rd

class DequeCheio(Exception):
    pass

class DequeVazio(Exception):
    pass

class Deque:
    def __init__(self, CAPACIDADE=3):
        self.capacidade = CAPACIDADE
        self.dados = [None] * self.capacidade
        self.tamanho = 0

    def __len__(self):
        return self.tamanho
    
    def isfull(self):
        return self.tamanho == self.capacidade
    
    def isempty(self):
        return self.tamanho == 0
    
    def add_last(self, elemento):
        try:
            if self.isfull() == False:
                self.dados[self.__len__()] = elemento
                self.tamanho += 1
            else:
                raise DequeCheio()
        except DequeCheio:
            print('O deque está cheio!')
    
    def add_first(self, elemento):
        try:
            if self.isfull() == False:
                if self.__len__() == 0:
                    self.dados[0] = elemento
                    self.tamanho += 1
                else:
                    posicao_atual = self.__len__()-1
                    for i in range(0, self.__len__()):
                        if self.dados[posicao_atual+1] == None:
                            temp = self.dados[posicao_atual]
                            self.dados[posicao_atual] = None
                            self.dados[posicao_atual+1] = temp
                        posicao_atual -= 1 
                    self.dados[0] = elemento
                    self.tamanho += 1
            else:
                raise DequeCheio()
        except DequeCheio:
            print('O deque está cheio!')

    def delete_first(self):
        try:
            if self.isempty():
                raise DequeVazio()
            else:
                self.dados[0] = None
                self.tamanho -= 1
                for i in range(0, self.__len__()):
                    if i < self.__len__():
                        if i == 0:
                            temp = self.dados[i+1]
                            self.dados[i+1] = None
                            self.dados[i] = temp
                        else:
                            temp = self.dados[i+1]
                            self.dados[i+1] = None
                            self.dados[i] = temp
        except DequeVazio:
            print('O deque está vazio!')

    def delete_last(self):
        try:
            if self.isempty():
                raise DequeVazio()
            else:
                last_data = self.__len__()-1
                self.dados[last_data] = None
                self.tamanho -= 1
        except DequeVazio:
            print('O deque está vazio!')

    def first(self):
        return self.dados[0]

    def last(self):
        last_data = self.__len__()-1
        return self.dados[last_data]
    
    def add_randon(self, elem):
        if rd(0,1) == 0:
            self.add_first(elem)
        else:
            self.add_last(elem)

    def delete_randon(self):
        if rd(0,1) == 0:
            self.delete_last()
        else:
            self.delete_first()

if __name__ == "__main__":
    pass