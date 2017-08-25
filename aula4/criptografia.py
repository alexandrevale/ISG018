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
                         "DP JSQBTKCIYHOVARZULENGXWMF")    

print ("Criptografar")
print encriptar(chave,"JAVA")
print encriptar(chave,"OLA MUNDO")
print encriptar(chave,"PHP")
print encriptar(chave,"PYTHON")

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

chave = montarDicionario2(" ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                         "DP JSQBTKCIYHOVARZULENGXWMF")    

print ("Decriptografar")
print encriptar(chave,"IPGP")
print encriptar(chave,"AHPDONVSA")
print encriptar(chave,"RKR")
print encriptar(chave,"RMEKAV")