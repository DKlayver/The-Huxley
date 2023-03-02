entrada=input().split()
lista=list()
for i in range(int(entrada[0])):
    lista.append(input())
lista.sort()
print(lista[int(entrada[1])-1])
