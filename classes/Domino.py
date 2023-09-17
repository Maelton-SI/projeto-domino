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

    def remove_proxima_peca(self):
        """
        Remove a proxima peça disponível do dominó e retorna seu valor.
        Retorna False se o dominó não possuir mais peças.
        """

        proxima_peca = self.pecas.head.getDados()
        
        if proxima_peca != None:
            self.pecas.head = self.pecas.head.getProximo()
            return proxima_peca
        else:
            return False

    def imprime_domino(self):
        noh_atual = self.pecas.head
        while noh_atual != None:
            print(noh_atual.getDados())
            noh_atual = noh_atual.getProximo()