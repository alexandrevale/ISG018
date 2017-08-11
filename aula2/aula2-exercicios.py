#Exercicio 1 - Faca um programa que digite dois nome, de mesmo tamanho, e mostre na tela um array contendo tuplas de letras de cada nome.
#Exemplo: "ANA" e "BOB"
#Resultado: [('A','B'),('N','O'),('A','B')]
nome1 = raw_input("Digite um nome: ")
nome2 = raw_input("Digite outro nome: ")
Aux = ()
for resultado in zip(nome1,nome2):
    Aux=Aux+resultado

print Aux
#print resultado
#print nome1
#print nome2

#Correcao
def ex2(n1,n2):
    if len(n1) == len(n2):
        auxiliar=[]
        for i in range(len(n1)):
            auxiliar.append((n1[i],n2[i]))
        print auxiliar
    else:
        print "Insira nome de msm tamanho."

n1 = raw_input("Digite um nome: ")
n2 = raw_input("Digite outro nome: ")
#Chamando a funcao
ex2(n1,n2)