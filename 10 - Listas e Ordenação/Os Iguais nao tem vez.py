vezes=int(input())
entrada=input().split()
lista=[int(i) for i in entrada]

for n in range(vezes):
    for i in lista:
        repetidos= lista.count(i)
        local= lista.index(i)
        localrepetido=None
        while repetidos>1:
            localrepetido=lista.index(i)
            lista.pop(localrepetido)
            repetidos-=1
lista.sort()
lista2=''
for p in lista:
    lista2=lista2 +' '+str(p)

print(lista2[1:])