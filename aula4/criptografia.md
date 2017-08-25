# Criptografia

## Introdução
Terminologias:
* Mensagem: informação a ser enviada. Em inglês, "plaintext".
* Texto cifrado: mensagem em tráfego, gerada por um algoritmo de engriptação. Em inglês, "ciphertext".
* Chave: pedaço de informação que mantém o segredo da encriptação. Em inglês, "key".
* Cifra: par de algoritmos de Encriptação e Decriptação.

As terminologias são representadas matematicamente por: 
* µ = Conjunto de mensagens
* χ = Conjunto de chaves
* ζ = Conjunto de textos gerados

Onde:
* E : χ * µ = ζ 
* D : χ * ζ = µ
 
Como devem ser:
* E(k,m) = c
* Equação de consistência para chaves simétricas -> D(k,E(k,m) = m