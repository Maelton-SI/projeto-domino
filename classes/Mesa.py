from estrutura_de_dados.Deque import *

class Mesa:
    def __init__(self):
        self.jogo = Deque()

    def imprime_jogo(self):
        return self.jogo.dados

