#Gere 5 bits aletorios a partir de: Xi+5 = Xi ^ Xi+1
def gRandom(seed):
    x = []
    for n in seed:
        x.append(int(n))
    i = 0
    while True:
        formula = x[i+1] ^ x[i]
        x.append(formula)
        i = i + 1
        yield formula

gerador = gRandom("00011")
aux = ""
for i in range(5):
    print gerador.next()