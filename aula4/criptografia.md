# Criptografia

## Introdução
Terminologias:
* Mensagem: informação a ser enviada. Em inglês, "plaintext".
* Texto cifrado: mensagem em tráfego, gerada por um algoritmo de engriptação. Em inglês, "ciphertext".
* Chave: pedaço de informação que mantém o segredo da encriptação. Em inglês, "key".
* Cifra: par de algoritmos de Encriptação e Decriptação.

As terminologias são representadas matematicamente por: 
* µ (m) = Conjunto de mensagens
* χ (k) = Conjunto de chaves
* ζ (c) = Conjunto de textos gerados

Onde:
* E : χ * µ = ζ 
* D : χ * ζ = µ
 
Como devem ser:
* E(k,m) = c
* Equação de consistência para chaves simétricas -> D(k,E(k,m) = m

## Cifras de Substituição
A partir de uma tabela K (chave) que faz correspondência em um alfabeto, o algoritmo faz a substituição letra à letra baseada na tabela.
A decriptação é executada de maneira inversa, "olhando a correspondência de trás para frente".
### Exemplo 1:
    seja Γ (Gama) um alfabeto...
    M = Γ * ( * indica todas as strings possíveis em Γ)
    C = Γ *
    K = {K:Γ -> Γ /K} é bijetora (pares), isto é, K: {0,1,2} -> {0,1,2} onde, K(0)=2, K(1)=0, K(2)=1,...

### Exemplo 2:
    Γ  = { , A, B, C, ..., Z}, total = 27

### Exemplo 3:
    k = |   | D |
        | A | P |
        | B |   |
        | C | J |
        | D | S |
        | E | Q |
        | F | B |
        | G | T |
        | H | K |
        | I | C |
        | J | I |
        | K | Y |
        | L | H |
        | M | O |
        | N | V |
        | O | A |
        | P | R |
        | Q | Z |
        | R | V |
        | S | L |
        | T | E |
        | U | N |
        | V | G |
        | W | X |
        | X | W |
        | Y | M |
        | Z | F |        
    
    E(k,m) = K(m1)||K(m2)...||K(mn)
    m = (m1)||(m2)...||(mn)
    m = Σ Γ
    D(k,c) = K-1(c1)||K-1(c2)...||K-1(mn)
    c = Σ Γ
    
    E(k, "JAVA") = K(J)||K(A)||K(V)||K(A) = IPGP
    D(k, "IPGP") = K(I)||K(P)||K(G)||K(P) = JAVA
    
### Exercício
* Usando K:
    * E (k, "Ola Mundo") = AHPDONVSA
    * E (k, "PHP") = RKR
    * E (k, "PYTHON") = RMEKAV
    * D (k, "KEOH") = HTML

Fato: a cifra de substituição é consistente.

**Ataque do Texto Cifrado Unico (Cipher Text Only Attack)**
1. Análise de frequência de letras
    
    |PT | EN|
    |   |   |
    | A | E |
    | E | T |
    | O | A |
    | S | O |
    | R | I |

2. Substituir a partir da frequência