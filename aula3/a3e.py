"""
Exercicio 1 - Faca uma funcao que receba duas palavras
e retorne um dicionario conforme o exemplo abaixo

"sol" "lua"
{'s':'l','o':'u','l':'a'}
"""

def exercicio1(p1,p2):
    d_aux = {}
    zipper = zip(p1,p2) #[('s', 'l'), ('o', 'u'), ('l', 'a')]
    for x in zipper:
        d_aux[x[0]] = x[1]  #'s':'l'
    return d_aux

palavra1 = raw_input("Digite a palavra 1:")
palavra2 = raw_input("Digite a palavra 2:")
print exercicio1(palavra1, palavra2)

#Outro jeito de resolver
def exercicio2(p1,p2):
    d_aux = {}
    zipper = zip(p1,p2) #[('s', 'l'), ('o', 'u'), ('l', 'a')]
    for (a,b) in zipper:
        d_aux[a] = b  #'s':'l'
    return d_aux

palavra1 = raw_input("Digite a palavra 1:")
palavra2 = raw_input("Digite a palavra 2:")
#print exercicio1(palavra1, palavra2)
print exercicio2(palavra1, palavra2)
