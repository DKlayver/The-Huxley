entrada=input().split()
linhasA=int(entrada[0])
colunasA_linhasB=int(entrada[1])
colunasB=int(entrada[2])

matrizA=[[int(i) for i in input().split()] for i in range(linhasA)]
matrizB=[[int(i) for i in input().split()] for i in range(colunasA_linhasB)]
matrizC=list()


B=list()
cont=0
for p in range(colunasB):

    for nmrB in range(colunasA_linhasB):
        B.append(matrizB[nmrB][cont])
    cont+=1

xing=0
matriz2=list()
for i in range(linhasA):
    lista_aux=list()
    for u in range(colunasA_linhasB):
        lista_aux.append(B[xing])
        xing+=1
    matriz2.append(lista_aux)



soma=0
multiplicacao=0
matrizSoma=list()
zun=0
for i in range(linhasA):
    listax=list()
    for j in range(linhasA):

        for u in range(colunasA_linhasB):
            multiplicacao=matrizA[i][u]*matriz2[j][u]
            soma+=multiplicacao
        listax.append(str(soma))
        soma=0
    matrizSoma.append(listax.copy())


for i in matrizSoma:
    print(' '.join(i))

