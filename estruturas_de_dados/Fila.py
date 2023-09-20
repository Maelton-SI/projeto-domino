class FilaVazia(Exception):
    pass

class Fila:
    def __init__(self, CAPACIDADE):
        self.capacidade = CAPACIDADE
        self.dados = [None * CAPACIDADE]
        self.tamanho = 0
        self.inicio = 0

    def __len__(self):
        return self.tamanho
    
    def enqueue(self, elemento):
        if self.tamanho == self.capacidade:
            self.aumenta_tamanho(2)
        else:
            espaco_disponivel = (self.inicio + self.tamanho) % self.capacidade
            self.dados[espaco_disponivel] = elemento
            self.tamanho += 1

    def aumenta_tamanho(self, multiplicador):
        fila_antiga = self.dados
        self.capacidade = self.capacidade * multiplicador
        self.dados = [None * self.capacidade]
        inicio_fila_antiga = self.inicio

        for _index in range(len(self.tamanho)):
            self.dados[_index] = fila_antiga[inicio_fila_antiga]
            inicio_fila_antiga = (inicio_fila_antiga + 1) % (self.capacidade / multiplicador)
        
        self.inicio = 0
        
    def diminui_tamanho(self, divisor):
        pass
    
    def dequeue(self):
        if self.is_empty():
            raise FilaVazia("A fila estah vazia!")
        else:
            elemento_removido = self.dados[self.inicio]
            self.dados[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.tamanho
            self.tamanho -= 1
            return elemento_removido

    def is_empty(self):
        return self.tamanho == 0
    
    def size(self):
        return self.tamanho

    def first(self):
        pass

if __name__ == "__main__":
    pass