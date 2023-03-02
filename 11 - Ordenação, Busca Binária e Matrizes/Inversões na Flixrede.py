quantidade=int(input())
lista=list()
cont=0
for i in range(quantidade):
    lista.append(int(input()))

for n in range(quantidade-1,0,-1):
    for p in range(i):
        if lista[p]>lista[p+1]:
            lista[p],lista[p+1]=lista[p+1],lista[p]
            cont+=1

print (cont)