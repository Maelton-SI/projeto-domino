from Fila import Fila

class Deque:
    def __init__(self, CAPACIDADE):
        self.dados = Fila(CAPACIDADE)
        self.tamanho = 0

    def __len__(self):
        return self.tamanho
    
    def add_last(self, elemento):
        self.dados.enqueue(elemento)
    
    def add_first(self):
        pass

    def delete_first(self):
        self.dados.dequeue()

    def delete_last(self):
        pass

    def first(self):
        pass

    def last(self):
        pass 