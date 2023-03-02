def ordenar_lista(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]

ListaMarilda=list()
ListaIrmao=list()

while True:
    entrada=input()
    if entrada=='FIM':
        break
    else:
        ListaMarilda.append(entrada)
ordenar_lista(ListaMarilda)
print("\n".join(ListaMarilda))
print('-'*50)

while True:
    entrada=input()
    if entrada=='FIM':
        break
    else:
        ListaIrmao.append(entrada)
ordenar_lista(ListaIrmao)
if ListaIrmao!=[]:
    print("\n".join(ListaIrmao))

print('-'*50)

ListaTOTAL=ListaMarilda+ListaIrmao
'''
for n in range(len(ListaTOTAL)-1,0,-1):
    for i in range(n):
        for j in range(i):
            if ListaTOTAL[i][j]>ListaTOTAL[i[j+1]]:
                ListaTOTAL[i][j], ListaTOTAL[i[j+1]]=ListaTOTAL[i[j+1]],ListaTOTAL[i][j]
'''
ordenar_lista(ListaTOTAL)
print("\n".join(ListaTOTAL))