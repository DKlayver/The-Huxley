while True:
    a,b=[int(i) for i in input().split()]
    if a==b==0:
        break
    repetidos={}
    for x in range(10):
            repetidos[str(x)]=0
    for i in range(a,b+1):
        for x in range(len(str(i))):
            repetidos[str(i)[x]]+=1
    listaREPETIDOS=[]
    for numero, repeticao in repetidos.items():
        listaREPETIDOS.append(str(repeticao))
    print(" ".join(listaREPETIDOS))