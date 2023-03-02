entrada=input().split()
linha = int(entrada[0])
coluna = int(entrada[1]) 
sequencia = list()

matriz = list()
for i in range(linha):
    lista = list()
    for u in input().split():
        lista.append(int(u))
    matriz.append(lista.copy())

for i in matriz:
    anterior=cont=seq=0
    for u in i:
        if u>=anterior:
            cont+=1
        else:
            cont=1
        if cont>seq:
            seq=cont
        anterior=u
    sequencia.append(seq)

for i in range(len(sequencia)):
    print("Linha %d: %d"%(i,sequencia[i]))

print("Maior Sequencia:",max(sequencia))