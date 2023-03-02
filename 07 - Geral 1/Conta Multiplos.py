valor1=int(input())
valor2=int(input())
resultado=0
memoria=0
contador=1
while contador<50:
    if contador%valor1==0 and contador%valor2==0:
        memoria+=1    
    contador+=1
print(memoria)