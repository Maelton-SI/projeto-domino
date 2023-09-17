from estrutura_de_dados.ListaEncadeada import ListaEncadeada
from estrutura_de_dados.Noh import Noh
from estrutura_de_dados.Deque import * 
class Domino:
    def __init__(self):
        self.pecas = self.gera_domino()
        self.embaralhadas = self.embaralha_domino()
    
    def gera_domino(self):
        pecas = ListaEncadeada()

        for lado_um in range(7):
            for lado_dois in range(lado_um, 7):
                peca = (lado_um, lado_dois)
                pecas.add(peca)
        
        return pecas
    
    def embaralha_domino(self):
        deque = Deque(28)
        self.pecas.emb(deque)
        return deque

    def size(self):
        pass

    def imprime_domino(self):
        noh_atual = self.pecas.head
        while noh_atual != None:
            print(noh_atual.getDados())
            noh_atual = noh_atual.getProximo()

