#"continue" interrompe a execucao de um unico ciclo.
print("Com continue")
i=0
while(i<10):
    i+=1
    if(i%2==0):
        continue   
    print(i)
else:
    print("")
#A instrucao "break" interrompe todos os ciclos.
print("Com break")
i=0
while(i<10):
    i+=1
    if(i%2==0):
        break   
    print(i)
else:
    print("")