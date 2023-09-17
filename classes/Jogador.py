from estrutura_de_dados.ListaEncadeada import ListaEncadeada

class Jogador():
    def __init__(self):
        self.nome = str()
        self.pontuacao = int()
        self.pecas = ListaEncadeada()
    
    def set_nome(self, nome):
        self.nome = nome
    
    def pega_peca(self, peca):
        self.pecas.add(peca)

    def jogar(self):
        pass

    def passar(self):
        pass

    def ganhar(self):
        #ganha se nao tiver mais pecas
        pass

    def imprime_pecas(self):
        self.pecas.imprime_lista_encadeada()


    