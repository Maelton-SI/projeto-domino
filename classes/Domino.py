from estrutura_de_dados.ListaEncadeada import ListaEncadeada
from estrutura_de_dados.Noh import Noh

class Domino:
    def __init__(self):
        self.pecas = self.gera_domino()
    
    def gera_domino(self):
        """
        Retorna uma lista encadeada, onde os valores dos nós são tuplas representando as peças de um dominó.
        """
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
            print(f"[{noh_atual.getDados()[0]}-{noh_atual.getDados()[1]}]")
            noh_atual = noh_atual.getProximo()

if __name__ == "__main__":
    pass