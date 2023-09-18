from estruturas_de_dados.ListaEncadeada import ListaEncadeada

class Jogador():
    def __init__(self):
        self.nome = str()
        self.pontuacao = int()
        self.pecas = ListaEncadeada()
    
    def set_nome(self, nome):
        self.nome = nome
    
    def pega_peca(self, peca):
        self.pecas.add(peca)

    def jogar(self, peca):
        pass

    def passar(self):
        pass

    def ganhar(self):
        #ganha se nao tiver mais pecas
        pass

    def imprime_pecas(self):
        noh_atual = self.pecas.head
        print(f"{self.nome}: ", end="")

        while noh_atual != None:
            print(f"[{noh_atual.getDados()[0]}-{noh_atual.getDados()[1]}] ", end="")
            noh_atual = noh_atual.getProximo()

if __name__ == "__main__":
    pass