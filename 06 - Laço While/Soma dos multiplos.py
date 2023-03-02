entrada=int(input())
contador=0
somatorio=0
while contador<entrada:
    if contador%3==0 or contador%5==0:
        somatorio=somatorio+contador
    contador=contador+1
print(somatorio)