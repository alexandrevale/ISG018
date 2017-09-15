#Gerador
def g1():
    yield 1
    yield 2
    yield 3
    yield 4

#Gerador sera um objeto da clase dos geradores
'''
gerador = g1()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
#print gerador.next()
'''
def g2():
    i=0
    while True: #loop infinito
        yield i
        i = i+2

gerador = g2()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()
print gerador.next()

        