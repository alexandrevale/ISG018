#Ler o arquivo csv (comma separeted value) e calcular a media
def calcularMedias():
    arq = open("alunos.dat","r") # r: read
    arq2 = open("saida.dat","w") # w: write
                                 # a: append
    linhas = arq.readlines()
    aux=""
    for l in linhas:
        tratarDados = l.rstrip() #remove o "\n"
        dados = tratarDados.split(',') #separa os dados em array
        media = (float(dados[1]) + float(dados[2]))/2
        if media >= 6:
            aux = aux + dados[0] + ": "+str(media)+ " = Passou \n"
        else:
            aux = aux + dados[0] + ": "+str(media)+ " = P3 \n"
    
    arq2.write(aux)
    arq.close()
    arq2.close()

calcularMedias()