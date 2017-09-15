import goslate

gs = goslate.Goslate()
#CONVERTENDO DE HEXADECIMAL PARA STRING 

c1 = "253a077715010b5e30011f68265302553f1f100d5f01511c50750e255d70003115432c04566c291c1c3646490c061a681d3054022524510c2b1f15144f0e00206b3b160a413f".decode("hex")
c2 = "283d17770a011b4575435b786b42090735095e17101a1754413d1c6d4138072415432103466c2a16192718491a12052d5b".decode("hex")
c3 = "392b1238041a01452c4d4b06241e4c1c224b43435e1a05581521112840354831140678025c6c231c00264a061c530b3e1c3955".decode("hex")
c4 = "3f37143215480d58360012383f121b1c2204100c5e105c005c381c6d42310c70110a2c0413382c164f310b040b53052d0c7b".decode("hex")
c5 = "283d17770f091e53751119292859091176014943531a15111b7530391523482309432b0d576d".decode("hex")
c6 = "253a07771001065830004b272d125e45675810145f071d1015360c3d1227013c0a433a09130d36140a2c1e0000124f".decode("hex")

#MOSTRANDO A FRASE CONVERTIDA E TIRANDO OS ESPACOS DAS FRASES
print "1 FRASE"
print "".join(c1.strip().lower().split())
print "2 FRASE"
print "".join(c2.strip().lower().split())
print "3 FRASE"
print "".join(c3.strip().lower().split())
print "4 FRASE"
print "".join(c4.strip().lower().split())
print "5 FRASE"
print "".join(c5.strip().lower().split())
print "6 FRASE"
print "".join(c6.strip().lower().split())

    
    
print "\nMENSAGENS DESCRIPTADAS EM INGLES "

# METODO PARA DESCRIPTAR
def otp (k,m,m2):
    z = zip(k,m,m2)
    aux = ""
    for (key,msg,msg2) in z:
        xr = ord(key) ^ ord(msg) ^ ord(msg2)
        aux = aux+chr(xr)
    return aux

# MENSAGENS DESCRIPTADAS EM INGLES
print "C1"
print otp(c1, c1, "The richest man is not he who has the most, but he who needs the least")

print "C2"
print otp(c1, c2, "The richest man is not he who has the most, but he who needs the least")

print "C3"
print otp(c1, c3, "The richest man is not he who has the most, but he who needs the least")

print "C4"
print otp(c1, c4, "The richest man is not he who has the most, but he who needs the least")

print "C5"
print otp(c1, c5, "The richest man is not he who has the most, but he who needs the least")

print "C6"
print 


    
# COMPROVANDO AS FRASES COM AS STRINGS

'''
def prova (k,m):
    z = zip(k,m)
    aux = ""
    for (key,msg) in z:
        xr = ord(key) ^ ord(msg)
        aux = aux+chr(xr)
    return aux
print prova("qRbWghh6UrkHK2luVl0c0uqt5UyM2PhPfcXl3LDsoBjinsnHuUtuMKqbNzqgozhEKWsk2K", c6)

#print otp(c1, c2,"The .")
'''
print (gs.translate(otp(c1, c6, "The richest man is not he who has the most, but he who needs the least"),'pt-br'))