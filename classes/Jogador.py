from estrutura_de_dados.ListaEncadeada import ListaEncadeada
from estrutura_de_dados.Deque import *

class Jogador():
    def __init__(self):
        self.nome = str()
        self.pontuacao = int()
        self.pecas = ListaEncadeada()
    
    def jogar(self, primeira_jogada):
        if primeira_jogada == True:
            pass
        else:
            pass

    def passar(self):
        pass

    def ganhar(self):
        #ganha se nao tiver mais pecas
        pass

    def imprime_pecas(self):
        self.pecas.imprime_lista_encadeada()


    