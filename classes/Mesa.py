from estrutura_de_dados.ListaEncadeada import ListaEncadeada
from classes.Domino import Domino
from classes.Jogador import Jogador

class Mesa():
    def __init__(self):
        self.domino = Domino()
        self.jogadores = ListaEncadeada()
        self.pecas = ListaEncadeada()

    def add_jogador(self, jogador):
        self.jogadores.add(jogador)
    
    def distribui_pecas_jogadores(self):
        self.domino.embaralha_domino()
        qtd_jogadores = len(self.jogadores)

        for _ in range(7):
            noh_jogador_atual = self.jogadores.head
            
            for jogadores in range(qtd_jogadores):
                jogador_atual = noh_jogador_atual.getDados()
                jogador_atual.pega_peca(self.domino.remove_proxima_peca())
                noh_jogador_atual = self.jogadores.head.getProximo()
    
    def imprime_pecas_jogadores(self):
        noh_jogador_atual = self.jogadores.head

        while noh_jogador_atual != None:
            jogador_atual = noh_jogador_atual.getDados()
            jogador_atual.imprime_pecas()

            noh_jogador_atual = noh_jogador_atual.getProximo()

if __name__ == "__main__":
    pass