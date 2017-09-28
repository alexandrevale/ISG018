import collections
import goslate

gs = goslate.Goslate()
texto = "QFI IPVJXU HVBFIZ XUHFVPI DUY VPSIPQIM LE U JIZXUP IPJVPIIZ, UZQFAZ YHFIZLVAY, DFT UBBGVIM NTZ FVY BUQIPQ TP NILZAUZE 23, 1918. QFVY DUY VP QFI YUXI QVXI NZUXI QFUQ 3 TQFIZ VPSIPQTZY NZTX 3 TQFIZ HTAPQZVIY UGYT UBBGVIM NTZ U BUQIPQ NTZ U ZTQUZE HVBFIZ XUHFVPI. YHFIZLVAY NVZYQ QZVIM QT YIGG FVY MIYVJP QT QFI JIZXUP XVGVQUZE LAQ NVPMVPJ PT VPQIZIYQ MIHVMIM QT YQUZQ AB FVY TDP HTXBUPE QT XUPANUHQAZI QFI IPVJXU NTZ HTXXIZHVUG YUGI. QFI IPVJXU XUHFVPI DUY NVZYQ TNNIZIM NTZ YUGI VP 1923, LAQ FUM NID QUWIZY. QFI IPVJXU XUHFVPI DUY UP VPJIPVTAY UMSUPHI VP QIHFPTGTJE, LTQF NTZ QFI YQZIPJQF TN QFI IPHVBFIZXIPQ UPM NTZ QFI IUYI TN AYI NTZ QFI TBIZUQTZ. VQ VY UP IGIHQZT-XIHFUPVHUG XUHFVPI ZIYIXLGVPJ U QEBIDZVQIZ, DVQF U BGAJLTUZM QT YDUB GIQQIZY, ZTQTZY QT NAZQFIZ YHZUXLGI QFI UGBFULIQ UPM U GUXB BUPIG QT MVYBGUE QFI ZIYAGQ. XTYQ XTMIGY TN IPVJXU AYIM 3 TZ 4 ZTQTZY DVQF U ZINGIHQTZ QT UGGTD QFI YUXI YIQQVPJY QT LI AYIM NTZ IPHVBFIZVPJ UPM MIHVBFIZVPJ"

contarCaract = collections.Counter(texto)

def decriptar(k,m):
    aux = "" # Texto cifrado
    for letra in m:
        # k[letra] olha na tabela
        aux = aux + k[letra]
    return aux

def montarDicionario2(gama1,gama2):
    if len(gama1)!=len(gama2):
        return {}
    else:
        dicionario = {}
        z = zip(gama1,gama2)
        for (x,y) in z:
            dicionario[y] = x
        return dicionario
        
# aprimorar metodo def contarCaractere(texto):
#    contador = 0
#    for letra in texto:
#        if letra == 'A':
#            contador = contador + 1
#    return contador

chave = montarDicionario2(" ETARINOSHMLCFPDGUWBYVKJXQZ,0123456789-.", #alfabeto texto
                          " IQUZVPTYFXGHNBMJADLESW____,0123456789-.") #alfabeto frequencia

#chave = montarDicionario2(" UXXXXHXXEXXBXFXRTXXOAIXXSR,0123456789-.",
                          #" ABCDEFGHIJKLMNOPQRSTUVWXYZ,0123456789-.")   

print 'Quantidade total de caracteres do texto: ' , len(texto)
print
print 'Quantidade total por caractere: ' , contarCaract.most_common(39)#39 caracteres
print 'Texto descriptografado: '
print
print decriptar(chave,texto)
print
print 'Texto traduzido: '
print
print (gs.translate(decriptar(chave, texto), 'pt-br'))