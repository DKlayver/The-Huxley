gabarito=input()
alunosProvas=dict()
entrada=input().split()
lista=list()

while True:
    if entrada[0]=='9999':
        break
    else:
        cont=0
        respostas=list(entrada[1])
        alunosProvas[entrada[0]]=entrada[1]
    
    for n in range(len(gabarito)):
        if respostas[n]==gabarito[n]:
            cont+=1
        else:
            continue
    print(entrada[0], float(cont))
    lista.append(cont)
    entrada=input().split()

aprovados=0
NotaFrequente=0

for j in lista:
    if j>=6:
        aprovados+=1
    else:
        continue   
percentual=('%.1f' % float((aprovados*100)/float(len(lista))))
print(str(percentual)+'%')    
notas_repetidas=0
for i in lista:
    if lista.count(i)>notas_repetidas:
        notas_repetidas=lista.count(i)
        NotaFrequente=i
    else:
        continue

print('%.1f'% NotaFrequente)
    