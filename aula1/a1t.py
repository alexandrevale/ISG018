#IT'S ALIVE!
print "Ola Mundo!"

#Calculos

#Adicao
x = int(raw_input("Digite n1: "))
y = int(raw_input("Digite n2: "))
soma = x + y
#Como "soma" eh int, nao eh necessaria a conversao, basta imprimir a variavel
print soma
#No exemplo abaixo, como o "Resultado: " eh necessario String e "soma" eh int, deve-se converter "soma" para String
print "Resultado: "+str(soma)

#Divisao
a = float(raw_input("Digite n1: "))
b = float(raw_input("Digite n2: "))
if b == 0:
    print "Erro"
#elif <condicao>:
else:
    divisao = a/b
    print "Resultado: "+str(divisao)