class Revolver:
    #atributo
    qtMunicao=0
    qtMax=0
    #metodo construtor
    """
    def __init__(self,qtMunicao,qtMax):
        self.qtMunicao = qtMunicao
        self.qtMax = 6        
    """
    #metodos
    def atirar(self):
        if self.qtMunicao==0:
            print "RELOAD"
        else:
            self.qtMunicao = self.qtMunicao-1
            print "BANG! | Vc ainda tem: ",str(self.qtMunicao)
    
    def recarregar(self):
        if self.qtMunicao < self.qtMax:
            print "Recarregado"
            self.qtMunicao = self.qtMunicao+1
            print "Vc ainda tem: ", str(self.qtMunicao)
        else:
            print("Sua pistola ta totalmente carregada.")

#municaoInicial = raw_input("Insira a quantidade de municao inicial: ")
#municaoMax = raw_input("Insira a quantidade maxima de municao da pistola: ")
pistola = Revolver()
pistola.atirar()
pistola.recarregar()