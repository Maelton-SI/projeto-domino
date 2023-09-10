class Noh:
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None

    def getDados(self):
        return self.dados
    
    def getProximo(self):
        return self.proximo
    
    def setDados(self, dados):
        self.dados = dados
    
    def setProximo(self, proximo):
        self.proximo = proximo