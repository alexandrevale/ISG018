def otp(k,m):
    z = zip(k,m)
    aux = ""
    for (key,msg) in z:
        xor = ord(key) ^ ord(msg) #ord pega o inteiro em ASCII
        aux = aux + chr(xor) # Return a string of one character whose ASCII code
    return aux.encode("hex") # decode
    
print otp("BCFF", "JAVA")
