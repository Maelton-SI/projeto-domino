from estrutura_de_dados.ListaEncadeada import ListaEncadeada
from estrutura_de_dados.Noh import Noh

class Domino:
    def __init__(self):
        self.pecas = self.gera_domino()
    
    def gera_domino(self):
        pecas = ListaEncadeada()

        for lado_um in range(7):

            for lado_dois in range(lado_um, 7):
                peca = (lado_um, lado_dois)
                pecas.add(peca)
        
        return pecas
    
    def embaralha_domino(self):
        pass

    def size(self):
        pass

    def imprime_domino(self):
        pass
