from estruturas_de_dados.ListaEncadeada import ListaEncadeada

class Jogador():
    def __init__(self):
        self.nome = str()
        self.pontuacao = int()
        self.pecas = ListaEncadeada()
        self.ganhou = False
    
    def set_nome(self, nome):
        self.nome = nome

    def get_ganhou(self):
        return self.ganhou
    
    def pega_peca(self, peca):
        self.pecas.add(peca)

    def get_qtd_pecas(self):
        return len(self.pecas)
    
    def joga_primeira_peca(self):
        """
        Retorna nó da primeira peça a ser jogada e retira nó das peças do jogador.
        Caso o jogador não tenha peça para jogar, retorna None.
        """

        peca = self.pecas.head
        self.pecas.head = self.pecas.head.getProximo()
        
        return peca
    
    def jogar(self, direita, esquerda):
        """
        Retorna nó da peça a ser jogada e retira nó das peças do jogador.
        Caso o jogador não tenha peça para jogar, retorna None.
        """
        noh_peca_anterior = None

        noh_peca_atual_jogador = self.pecas.head
        while noh_peca_atual_jogador != None:
            peca_atual = noh_peca_atual_jogador.getDados()
            
            if peca_atual[0] == direita:
                if noh_peca_atual_jogador.getProximo() == None: self.ganhar()
                self.pecas.remove(peca_atual)
                
                return noh_peca_atual_jogador
            
            elif peca_atual[0] == esquerda:
                if noh_peca_atual_jogador.getProximo() == None: self.ganhar()
                self.pecas.remove(peca_atual)

                return noh_peca_atual_jogador
            
            elif peca_atual[1] == direita:
                if noh_peca_atual_jogador.getProximo() == None: self.ganhar()
                self.pecas.remove(peca_atual)
                
                return noh_peca_atual_jogador
            
            elif peca_atual[1] == esquerda:
                if noh_peca_atual_jogador.getProximo() == None: self.ganhar()
                self.pecas.remove(peca_atual)
                
                return noh_peca_atual_jogador
            
            noh_peca_atual_jogador = noh_peca_atual_jogador.getProximo()
        
        return None

    def ganhar(self):
        self.ganhou = True
        pass

    def imprime_pecas(self):
        noh_atual = self.pecas.head
        print(f"{self.nome}: ", end="")

        while noh_atual != None:
            print(f"[{noh_atual.getDados()[0]}-{noh_atual.getDados()[1]}] ", end="")
            noh_atual = noh_atual.getProximo()

    def get_somatorio_pecas(self):
        """
        Retorna o somatorio dos valores das peças do jogador.
        """
        somatorio = int()

        noh_peca_atual_jogador = self.pecas.head
        while noh_peca_atual_jogador != None:
            peca_atual = noh_peca_atual_jogador.getDados()

            somatorio += int(peca_atual[0]) + int(peca_atual[1])
        
        return somatorio

if __name__ == "__main__":
    pass