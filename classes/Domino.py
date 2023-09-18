from estruturas_de_dados.ListaEncadeada import ListaEncadeada
from estruturas_de_dados.Noh import Noh
from estruturas_de_dados.Deque import Deque
from random import randint

class Domino:
    def __init__(self):
        self.pecas = self.gera_domino()

    def setPecas(self, pecas):
        self.pecas = pecas
    
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
            
    def embaralha_domino(self):
        def converte_lista_domino_em_deque_embaralhado():
            deque_auxiliar_um = Deque()

            while self.pecas.head != None:
                peca_atual = self.remove_proxima_peca()

                if randint(0,100) % 2 == 0:
                    deque_auxiliar_um.add_last(peca_atual)
                else:
                    deque_auxiliar_um.add_first(peca_atual)
            
            deque_auxiliar_dois = Deque()

            while not deque_auxiliar_um.is_empty():
            
                if randint(0,100) % 2 == 0:
                    peca_atual = deque_auxiliar_um.last()
                    deque_auxiliar_um.delete_last()

                    if randint(0,100) % 2 == 0:
                        deque_auxiliar_dois.add_first(peca_atual)
                    else:
                        deque_auxiliar_dois.add_last(peca_atual)
                else:
                    peca_atual = deque_auxiliar_um.first()
                    deque_auxiliar_um.delete_first()

                    if randint(0,100) % 2 == 0:
                        deque_auxiliar_dois.add_first(peca_atual)
                    else:
                        deque_auxiliar_dois.add_last(peca_atual)
            
            return deque_auxiliar_dois
        
        def converte_deque_em_lista_domino_embaralhado(deque):
            domino_embaralhado = ListaEncadeada()

            while not deque.is_empty():
                if randint(0,100) % 2 == 0:
                    peca_atual = deque.last()
                    deque.delete_last()

                    domino_embaralhado.add(peca_atual)
                else:
                    peca_atual = deque.first()
                    deque.delete_first()

                    domino_embaralhado.add(peca_atual)
            
            return domino_embaralhado
        
        deque_embaralhado = converte_lista_domino_em_deque_embaralhado()
        domino_embaalhado = converte_deque_em_lista_domino_embaralhado(deque_embaralhado)

        self.setPecas(domino_embaalhado)
        

    def imprime_domino(self):
        noh_atual = self.pecas.head
        while noh_atual != None:
            print(f"[{noh_atual.getDados()[0]}-{noh_atual.getDados()[1]}]")
            noh_atual = noh_atual.getProximo()

if __name__ == "__main__":
    pass