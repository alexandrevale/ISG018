#Gere 6 bits aletórios a partir de: Xi+2 = Xi ^ Xi+1
def g3(seed):
    x = []
    for n in seed:
        x.append(int(n))
    i = 0
    while True:
        formula = x[i+1] ^ x[i]
        x.append(formula)
        i = i + 1
        yield formula

gerador = g3("11")
'''
for i in range(6):
    print gerador.next()
'''
print "Digite a quantidade: "
n = int(raw_input())
for i in range(n):
    print gerador.next()