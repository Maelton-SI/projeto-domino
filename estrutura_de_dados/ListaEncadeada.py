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
        self.size =+ 1 
    
    def __len__(self):
        return self.size