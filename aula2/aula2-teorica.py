#Vetor
v = []
#Inserindo elementos no vetor
v.append('Alexandre')
v.append(28)
v.append(True)
v.append([1,2,3])
v.append([])
print str("Imprimindo o vetor")
print v

#Exemplo 1
#"For" para exibir os elementos
print str("Imprimindo o vetor, elemento por elemento")
for e in v:
    print e

#"For" com indice
print str("Imprimindo o vetor, elemento por elemento, com indice")
for i in range(len(v)):
# range(len(v)) = range(5), onde range(5) = [0,1,2,3,4]
    print str(i)+" -> "+str(v[i])

#Exemplo 2
v2 = range(9)
print str("Imprimindo o vetor completo (9): ")+str(v2)
print str("Tudo entre indice 2 ao 5: ")+str(v2[2:5]) 
print str("Ignora tudo ate o terceiro indice: ")+str(v2[3:])
print str("Tudo ate o indice 6: ")+str(v2[:7])
print str("Imprime o utlimo valor: ")+str(v2[-1:])

#Para estudar: https://www.quantopian.com/lectures

#Exemplo 3
v2[3] = "Alterar o valor"
print v2

#Diferenca entre vetor e tuple
#A tuple is a sequence of immutable Python objects. 
#The differences between tuples and lists are, the tuples cannot be changed unlike lists 
#and tuples use parentheses, whereas lists use square brackets.

#Exemplo 4
palavra1 = raw_input("Digite uma palavra: ")
print "Reverso: ",palavra1[::-1]
#Tambem podemos fazer com for
palavra2 = raw_input("For sem indice -> Digite um palavra: ")
aux = ""
for letra in palavra2:
    aux=letra+aux
print aux

palavra3 = raw_input("For sem indice -> Digite um palavra: ")
aux2 = ""
for i in range(len(palavra3)):
    aux2=palavra3[i]+aux2
print str(aux2)

#Funcao
def somar(x,y):
    return x+y