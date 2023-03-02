entrada=int(input())

for cont in range(entrada+1):
    anterior=cont*cont
    if cont!=0:
        print(cont, (cont*cont), cont*anterior)