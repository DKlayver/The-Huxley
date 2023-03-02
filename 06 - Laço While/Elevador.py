valores=input().split()
leitura,capacidade=int(valores[0]), int(valores[1])
total=0
excedido='N'
while leitura>0:
    entradas=input().split()
    sairam,entraram,=int(entradas[0]),int(entradas[1])
    total=total-sairam
    total=total+entraram
    if total>capacidade:
        excedido='S'
    leitura-=1
print(excedido)