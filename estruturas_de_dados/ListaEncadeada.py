from estruturas_de_dados.Noh import Noh

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head == None

    def add(self, elemento):
        novo_noh = Noh(elemento)
        novo_noh.setProximo(self.head)
        self.head = novo_noh
        self.size += 1 
    
    def remove(self, valor_noh):
        if self.head == None:
            print("{} is not in list".format(valor_noh))
        elif self.head.getDados() == valor_noh:
            self.head = self.head.getProximo()
            self.size -= 1
        else:
            ancestor = self.head
            ponteiro = self.head.getProximo()
            removeu = False
            while(ponteiro):
                if ponteiro.getDados() == valor_noh:
                    ancestor.setProximo(ponteiro.getProximo())
                    ponteiro.setProximo(None)
                    self.size -= 1
                    removeu = True
                    break
                
                ancestor = ponteiro
                ponteiro = ponteiro.getProximo()
            if not removeu:
                print("{} is not in list".format(valor_noh))
    
    def __len__(self):
        return self.size
    
    def imprime_lista_encadeada(self):
        peca_atual = self.head.getDados()
        for i in range(0, self.size):
            if i == 0:
                print(peca_atual, end='')
                peca_atual = self.head.getProximo()
            else:
                print(peca_atual.getDados(), end='')
                peca_atual = peca_atual.getProximo()
        print()

    def get_ultimo_noh(self):
        return self.head
            
if __name__ == "__main__":
    pass