#Ex1 Faca um programa que decide o maior entre dois numeros digitados pelo usuario
print "Qual o n maior?"
x = int(raw_input("Digite n1: "))
y = int(raw_input("Digite n2: "))
if x > y:
    print "O maior: "+str(x)
else:
    print "O maior: "+str(y)

#Ex2 Faca um programa que verifica que uma String digitada eh vazia ou nao
print "Verifique sua mensagem"
msg = str(raw_input("Insire uma mensagem: "))
if not msg: #Outra forma seria if x == "":
    print "Por favor, digite uma mensagem"
else:
    print msg