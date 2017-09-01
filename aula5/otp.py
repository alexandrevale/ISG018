def otp(k,m):
    z = zip(k,m)
    aux = ""
    for (key,msg) in z:
        xor = ord(key) ^ ord(msg) #ord pega o inteiro em ASCII
        aux = aux + chr(xor) # ???
    return aux.encode("hex")
    
print otp("BCFF", "JAVA")