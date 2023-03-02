quantidade=int(input())
entrada1=input().split()
entrada2=input().split()
candidato=[float(i) for i in entrada1]
concorrente=[float(i) for i in entrada2]
lista=list()
maior=0
for p in range(quantidade):
    
    diferenca= (candidato[p]-concorrente[p])
    if diferenca>0 and diferenca>maior:
        lista.append(diferenca)
if diferenca>0:
    print('%.2f'% max(lista))
else:
    print('0.00')
