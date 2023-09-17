from estrutura_de_dados.Noh import Noh

class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head == None

    def add(self, item):
        novo_noh = Noh(item)
        novo_noh.setProximo(self.head)
        self.head = novo_noh
        self.size += 1 
    
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

    def emb(self,d):
        peca_atual = self.head.getDados()
        for i in range(0, 28):
            if i == 0:
                print(peca_atual)
                d.add_randon(peca_atual)
                peca_atual = self.head.getProximo()
            else:
                print(peca_atual.getDados())
                d.add_randon(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
    
    def remove(self, elem):
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.getDados() == elem:
            print(f"{self.head.getDados()} removido!")
            self.head = self.head.getProximo()
            self.size =- 1
        else:
            ancestor = self.head
            ponteiro = self.head.getProximo()
            while(ponteiro):
                if ponteiro.getDados() == elem:
                    print(f"{ponteiro.getDados()} removido!")
                    ancestor.setProximo(ponteiro.getProximo())
                    ponteiro.setProximo(None)
                    self.size =- 1
                    return True
           
                ancestor = ponteiro
                ponteiro = ponteiro.getProximo()
            raise ValueError("{} is not in list".format(elem))  
        