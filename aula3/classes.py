class Contador:
    #atributo
    qtPessoas=0
    #metodo construtor
    def __init__(self,qtPessoas):
        self.qtPessoas = qtPessoas
    #metodos
    def incrementar(self):
        #self semelhante ao this
        self.qtPessoas = self.qtPessoas+1

    def decrementar(self):
        #self semelhante ao this
        self.qtPessoas = self.qtPessoas-1
        
    def zerar(self):
        #self semelhante ao this
        self.qtPessoas = 0
    
    def mostrar(self):
        print self.qtPessoas

k=Contador(10)
k.incrementar() #11
k.incrementar() #12
k.incrementar() #13
k.decrementar() #12
k.mostrar()
k.decrementar() #11
k.mostrar()