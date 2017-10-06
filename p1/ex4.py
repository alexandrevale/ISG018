#Encriptar
def encriptar(k,m):
    # Onde "m = String" e "k = Dicionario"
    aux = "" # Texto cifrado
    for letra in m:
        # k[letra] olha na tabela
        aux = aux + k[letra]
    return aux

def montarDicionario(gama1,gama2):
    if len(gama1)!=len(gama2):
        return {}
    else:
        dicionario = {}
        z = zip(gama1,gama2)
        for (x,y) in z:
            dicionario[x] = y
        return dicionario

chave = montarDicionario(" ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                         " PYDCLKHMZXREGVWAUFTSQNOJBI")    

print ("Criptografar")
print encriptar(chave,"ATAQUE HOJE")


def decriptar(k,m):
    aux = "" # Texto cifrado
    for letra in m:
        # k[letra] olha na tabela
        aux = aux + k[letra]
    return aux

def montarDicionario2(gama1,gama2):
    if len(gama1)!=len(gama2):
        return {}
    else:
        dicionario = {}
        z = zip(gama1,gama2)
        for (x,y) in z:
            dicionario[y] = x
        return dicionario

chave = montarDicionario("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                         "PYDCLKHMZXREGVWAUFTSQNOJBI")  

print ("Decriptografar")
print encriptar(chave,"GPTG")
print encriptar(chave,"PLT")
print encriptar(chave,"DLPTPK")
print encriptar(chave,"KPVCWV")