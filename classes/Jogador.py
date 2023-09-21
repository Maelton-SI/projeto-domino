from estruturas_de_dados.ListaEncadeada import ListaEncadeada
class Tipo(type):
    def __repr__(self):
        return self.__name__

class Jogador(metaclass = Tipo):
    def __init__(self, nome=str()):
        self.nome = nome
        self.pontuacao = int()
        self.pecas = ListaEncadeada()
        self.ganhou = False
    
    def get_proxima_peca(self):
        if len(self.pecas) != 0:
            return self.pecas.head.getDados()
        
    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def get_ganhou(self):
        return self.ganhou
    
    def pega_peca(self, peca):
        """
        Recebe os valores de uma peça e adiciona às peças do jogador.
        """
        self.pecas.add(peca)

    def get_qtd_pecas(self):
        return len(self.pecas)
    
    def jogar(self, direita, esquerda):
        """
        Retorna nó da peça a ser jogada e retira nó das peças do jogador.
        Caso o jogador não tenha peça para jogar, retorna None.
        """
        noh_peca_anterior = None

        noh_peca_atual_jogador = self.pecas.head
        while noh_peca_atual_jogador != None:
            peca_atual = noh_peca_atual_jogador.getDados()

            if peca_atual[0] == direita or peca_atual[0] == esquerda:
                if self.get_qtd_pecas() == 1: self.ganhar()
                self.pecas.remove(peca_atual)
                
                return noh_peca_atual_jogador
            
            elif peca_atual[1] == direita or peca_atual[1] == esquerda:
                if self.get_qtd_pecas() == 1: self.ganhar()
                self.pecas.remove(peca_atual)
                
                return noh_peca_atual_jogador
            
            noh_peca_atual_jogador = noh_peca_atual_jogador.getProximo()
        
        return None

    def ganhar(self):
        self.ganhou = True

    def imprime_pecas(self):
        noh_atual = self.pecas.head
        print(f"{self.nome}: ", end="")

        while noh_atual != None:
            print(f"[{noh_atual.getDados()[0]}-{noh_atual.getDados()[1]}] ", end="")
            noh_atual = noh_atual.getProximo()
        
        print()
    
    def get_somatorio_pecas(self):
        """
        Retorna o somatorio dos valores das peças do jogador.
        """
        somatorio = int()

        noh_peca_atual_jogador = self.pecas.head
        # while noh_peca_atual_jogador != None:
        # print(self.pecas.size)
        for i in range(0, self.pecas.size):
            # print('entrou no somatório')
            peca_atual = noh_peca_atual_jogador.getDados()

            somatorio += (peca_atual[0] + peca_atual[1])
            noh_peca_atual_jogador = noh_peca_atual_jogador.getProximo()
        return somatorio

if __name__ == "__main__":
    pass