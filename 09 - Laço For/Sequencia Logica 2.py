entrada=input().split()
x=int(entrada[0])
y=int(entrada[1])
import math
memoria1=''
memoria2=''
regredir=  math.ceil(y/x)
vezes=0
contador=0
for cont in range(1,regredir):
    while vezes<x and contador<y:
        contador+=1
        memoria1=memoria1+' '+str(contador)
        vezes+=1
    print(memoria1.strip())
    memoria1=memoria2
    vezes=0
    while vezes<x and contador<y:
        contador+=1
        memoria2=memoria2+' '+str(contador)
        vezes+=1
    print(memoria2.strip())
    memoria2=memoria1
    vezes=0
    
    