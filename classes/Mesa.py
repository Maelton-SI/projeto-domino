from estruturas_de_dados.ListaEncadeada import ListaEncadeada
from estruturas_de_dados.Deque import Deque
from classes.Domino import Domino
from classes.Jogador import Jogador

class Mesa():
    def __init__(self):
        self.domino = Domino()
        self.jogadores = ListaEncadeada()

        self.pecas = Deque()
        self.extremidade_direita = None
        self.extremidade_esquerda = None

        self.ganhador = False  

    def set_ganhador(self, ganhador):
        self.ganhador = ganhador
    
    def get_ganhador(self):
        return self.ganhador
    
    def add_jogador(self, jogador):
        self.jogadores.add(jogador)
    
    def distribui_pecas_jogadores(self):
        self.domino.embaralha_domino()
        
        for _ in range(7):
            qtd_jogadores = len(self.jogadores)
            noh_jogador_atual = self.jogadores.head
            
            for jogadores in range(qtd_jogadores):
                jogador_atual = noh_jogador_atual.getDados()
                jogador_atual.pega_peca(self.domino.remove_proxima_peca())

                noh_jogador_atual = noh_jogador_atual.getProximo()

    def imprime_pecas_jogadores(self):
        noh_jogador_atual = self.jogadores.head

        print()
        while noh_jogador_atual != None:
            jogador_atual = noh_jogador_atual.getDados()
            jogador_atual.imprime_pecas()

            noh_jogador_atual = noh_jogador_atual.getProximo()
    
    def imprime_mesa(self):
        self.imprime_pecas_jogadores()
        print()
        
        print('Jogo: ', end='')
        for i in range(0, self.pecas.tamanho):
            print(f'[{self.pecas.dados[i][0]}-{self.pecas.dados[i][1]}] ', end='')
        print()
    
    def get_extremidade_direita(self):
        """
        Retorna valor da extremidade direita das peças do jogo na mesa.
        Retorna None caso não ainda não existam peças na mesa.
        """
        return self.pecas.last()[1] if len(self.pecas) else None

    def set_extremidade_direita(self):
        self.extremidade_direita = self.get_extremidade_direita()

    def get_extremidade_esquerda(self):
        """
        Retorna valor da extremidade esquerda das peças do jogo na mesa.
        Retorna None caso não ainda não existam peças na mesa.
        """

        return self.pecas.first()[0] if len(self.pecas) else None
    
    def set_extremidade_esquerda(self):
        self.extremidade_esquerda = self.get_extremidade_esquerda()

    def get_extremidades(self):
        """
        Retorna tupla contendo os valores das duas extremidades do conjunto de peças na mesa.
        A tupla contem a extremidade de menor valor na posição 0 e a extremidade de maior valor na posição 1.

        Retorna None caso ainda não existam peças do jogo na mesa.
        """
        if len(self.pecas) == 1:
            peca = self.pecas.first()
            
            if peca[0] == peca[1]: return peca
            elif peca[0] > peca[1]: return (peca[1], peca[0])
            else: return (peca[0], peca[1])

        elif len(self.pecas) > 1:
            extremidade_direita = self.get_extremidade_direita()
            extremidade_esquerda = self.get_extremidade_esquerda()

            if extremidade_esquerda == extremidade_direita: 
                return (extremidade_esquerda, extremidade_direita)
            
            elif extremidade_esquerda > extremidade_direita: 
                return (extremidade_direita, extremidade_esquerda)

            else: 
                return (extremidade_esquerda, extremidade_direita)
        else:
            return None

    def add_peca(self, noh_peca):
        if len(self.pecas) == 0:
            peca = noh_peca.getDados()
            self.pecas.add_last(peca)
            
        else:
            peca = noh_peca.getDados()

            if peca[0] == self.get_extremidade_direita():
                self.pecas.add_last(peca)
                
            elif peca[0] == self.get_extremidade_esquerda():
                self.pecas.add_first((peca[1], peca[0]))
            
            elif peca[1] == self.get_extremidade_direita():
                self.pecas.add_last((peca[1], peca[0]))
            
            elif peca[1] == self.get_extremidade_esquerda():
                self.pecas.add_first(peca)

    def rodada(self):
        self.imprime_mesa()

        alguem_jogou = False

        noh_atual_jogador = self.jogadores.head
        
        if len(self.pecas) == 0:
            jogador_atual = noh_atual_jogador.getDados()
            peca_jogada = jogador_atual.jogar(jogador_atual.get_proxima_peca()[0], 
                                                jogador_atual.get_proxima_peca()[1])
            
            self.add_peca(peca_jogada)
            noh_atual_jogador = noh_atual_jogador.getProximo()

        while noh_atual_jogador != None:
            if self.get_ganhador():
                break
            
            jogador_atual = noh_atual_jogador.getDados()
            peca_jogada = jogador_atual.jogar(self.get_extremidade_direita(), 
                                                self.get_extremidade_esquerda())
            
            if peca_jogada:
                self.add_peca(peca_jogada)
                alguem_jogou = True
                
                if jogador_atual.get_ganhou():
                    self.set_ganhador(jogador_atual)
                    # print(f"{jogador_atual.get_nome()} ganhou!")
                    break
            
            noh_atual_jogador = noh_atual_jogador.getProximo()

        if not alguem_jogou:
            return "EMPATE", self.jogadores
          
        elif self.get_ganhador():
            return self.get_ganhador()
          
        else:
            return False
        
    def compara_pecas(self):
        menor_somatorio_pecas = 67

        noh_atual_jogador = self.jogadores.head

        while noh_atual_jogador != None:

            jogador_atual = noh_atual_jogador.getDados()
            peca_jogada = jogador_atual.jogar(self.get_extremidade_direita(), 
                                                self.get_extremidade_esquerda())
            
            if peca_jogada:
                self.add_peca(peca_jogada)
                alguem_jogou = True
                
                if jogador_atual.get_ganhou():
                    self.set_ganhador(jogador_atual)
                    print(f"{jogador_atual.get_nome()} ganhou!")
                    break
            
            noh_atual_jogador = noh_atual_jogador.getProximo()

if __name__ == "__main__":
    pass