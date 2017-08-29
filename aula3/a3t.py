#Dicionario - Container nao ordenado
def dicionario():
    d = {} #dicionario vazio
    d["Algo"] = 7
    d[9] = 7.5
    d[7.5] = True
    d[(1,2,3,4)] = 'W'
    d[1] = [1,"Dois",3]
    print d
    obj = {"nome":"Alexandre", "idade":28}
    print obj

#dicionario()

def dicionario2(dic):
    for i in dic:
        #print i
        print(str(i)+" -> "+str(dic[i]))
        
dicionario2({"indice": "valor",
            7:"Algo",
            True:4,
            1.1:(3,4,5)
            })
#Funcao e Dicionario são isomorfos