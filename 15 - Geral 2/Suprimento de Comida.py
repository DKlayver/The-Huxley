testes=int(input())

for x in range(testes):
    comida=float(input())
    cont=0
    while comida>1:
        comida/=2
        cont+=1
    print(cont,"dias")