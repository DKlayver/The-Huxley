vezes=int(input())
cardapio=dict()

for i in range(vezes):
    codigo=input()
    cardapio[codigo] = input(), float(input())
    
#print (cardapio)

lista=list()
while True:
    
    entrada=input()
    if entrada=='0':
        print('%.2f' % sum(lista))
        break
    
    else:
        quantidade=int(input())
        if entrada in cardapio and quantidade>0:
            x=cardapio.get(entrada, 'error')
            multi=x[1]*quantidade
            lista.append(multi)