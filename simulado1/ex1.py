#Encriptar
def e(k,m):
    aux = ""
    for letra in m:
        aux = aux + k[letra]
    return aux

def getKeyE():
    keyE = {}
    alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    beta = 'PYDCLKHMZXREGVWAUFTSQNOJBI'
    z = zip(alfa,beta)
    for x,y in z:
        keyE[x] = y
    return keyE

def getKeyD():
    keyD = {}
    alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    beta = 'PYDCLKHMZXREGVWAUFTSQNOJBI'
    z = zip(alfa,beta)
    for x,y in z:
        keyD[y] = x
    return keyD

def d(k,m):
    aux = ""
    for letra in m:
        aux = aux + k[letra]
    return aux  

print e(getKeyE(),"FATEC")
print e(getKeyE(),"PRAIA")
print d(getKeyD(),"XPNP")
print d(getKeyD(),"ABSMWV")