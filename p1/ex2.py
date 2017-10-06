#Gere 5 bits aletorios a partir de: Xi+5 = Xi+1 ^ Xi+2 ^ Xi+3 ^ Xi
def gRandom(seed):
    x = []
    for n in seed:
        x.append(int(n))
    i = 0
    while True:
        formula = x[i+1] ^ x[i]+2 ^ x[i+3] ^ x[i]
        x.append(formula)
        i = i + 1
        print " "
        yield formula

gerador = gRandom("00010")
aux = ""
for i in range(5):
    print gerador.next()