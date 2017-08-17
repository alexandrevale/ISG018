"""
Pilha (Stack) FILO
Array - estrutura de dados estatica para manipulacao de um numero finito de elementos
Set - estrutura de dados que tem como principio conter uma lista de valores diferentes
"""
lista = [1,2,3,4,5]
print(type(lista))
print(lista)
#acessando com len
elementos = lista[len(lista)-1]
print(elementos)
print(lista[3])
print("")
tupla = (1,2,3,4,5)
print(type(tupla))
print(tupla)
print("Op entre lista e tupla")
print(lista[2]+tupla[4])

dados = list("Winter")
print(dados)
print(dados[0])
print(dados[1])
print(dados[2])
dados = list(("Winter",))
print(dados)