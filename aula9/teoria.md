# Criptografia de Chave Pública

Conjuntos: inteiros, racionais, irracionais, reais, imaginários.

## Anéis dos Inteiros

Definição de anél: conjunto A que possui duas operações binárias: adição e multiplicação, que satisfazem os axiomas. 
Axiomas são verdades inquestionáveis universalmente válidas, muitas vezes utilizadas como princípios na construção de uma teoria ou como base para uma argumentação. 

Para adição:

* Associativa: (a + b) + c = a + (b + c)
* Neutro (zero): a + 0 = 0 + a = a
* Oposto: a + (-a) = (-a) + a
* Comutatividade: a + b = b + a
 
Para multiplicação:

* Associativa: (a . b) . c = a . (b . c)
* Unidade: a . 1 = 1 . a
* Comutatividade: a . b = b . a
* Inverso: a . a^-1 = a^-1 . a = 1
 
Exemplo:
Z(4) = {0, 1, 2, 3}

| + | 0 | 1 | 2 | 3 |
| 0 | 0 | 1 | 2 | 3 |
| 1 | 1 | 2 | 3 | 0 |
| 2 | 2 | 3 | 0 | 1 |
| 3 | 3 | 0 | 1 | 2 |


| . | 0 | 1 | 2 | 3 |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 2 | 3 |
| 2 | 0 | 2 | 0 | 2 |
| 3 | 0 | 3 | 2 | 1 |

2 + 2 === 0 (mod 4)
3 . 3 === 1 (mod 4) 
2 - 3 === 2 + 1 === 3 (mod 4)

Quem é o oposto de Z(4)?
    O oposto de 0 é 0
    O oposto de 1 é 3
    O oposto de 2 é 2
    O oposto de 3 é 1

Exemplo:

2 - 7 === 2 + 2 === 4 (mod 9)

Isso ocorre porque o oposto de 7 é 2 (7 + 2 = 9)

Exemplo: 

3 - 11 === 12 (mod 20)

Método rápido: 3 - 11 = -8, -8 + 20 = 12