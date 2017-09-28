# Cifras de Fluxo

## Gerador de números pseudo aleatórios
SEED (semente) dispara o algoritmo conforme esta informação. Será usada como chave.
E(k,m) = m ^ GNPA(k)

Onde,
* GNPA: Gerador de números pseudo aleatórios
* k é a seed/chave

## Algoritmos

### LFSR (Linear Feedback Shift Register)
Gera bits aleatórios de acordo com uma relação de recorrência

#### Exemplo
Gere 4 bits aleatórios a partir de:
* Xi+4 = Xi+3 ^ Xi
Necessário prover 4 bits de seed (2 elevado a 4 = 16 diferentes)

X = 0110, X0 = 0, X1 = 1, X2 = 1, X3 = 0
Para i = 0 -> X4 = X3 ^ X0 = 0 ^ 0 = 0
Para i = 1 -> X5 = X4 ^ X1 = 0 ^ 1 = 1
Para i = 2 -> X6 = X5 ^ X2 = 1 ^ 1 = 0
Para i = 3 -> X7 = X6 ^ X3 = 0 ^ 0 = 0

Resposta: 0100

#### Exercício
Gere 6 bits aletórios a partir de:
* Xi+2 = Xi ^ Xi+1

X = 11, X0 = 1, X1 = 1
Para i = 0 -> X2 = X1 ^ X0 = 1 ^ 1 = 0
Para i = 1 -> X3 = X2 ^ X1 = 0 ^ 1 = 1
Para i = 2 -> X4 = X3 ^ X2 = 1 ^ 0 = 1
Para i = 3 -> X5 = X4 ^ X3 = 1 ^ 1 = 0
Para i = 4 -> X6 = X5 ^ X4 = 0 ^ 1 = 1
Para i = 5 -> X7 = X6 ^ X5 = 1 ^ 0 = 1

Resposta: 011011