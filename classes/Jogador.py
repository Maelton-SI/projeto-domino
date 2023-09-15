from estrutura_de_dados.ListaEncadeada import ListaEncadeada

class Jogador():
    def __init__(self):
        self.nome = str()
        self.pontuacao = int()
        self.pecas = ListaEncadeada()
    
    def imprime_pecas(self):
        peca_atual = self.pecas.head.getDados()
        for i in range(0, self.pecas.size):
            if i == 0:
                print(peca_atual, end='')
            else:
                peca_atual = peca_atual.getProximo()
                print(peca_atual.getDados(), end='')

    
    def jogar(self):
        pass

    def passar(self):
        pass

    def ganhar(self):
        #ganha se nao tiver mais pecas
        pass

    