entrada=int(input())
par=0
impar=0
positivo=0
negativo=0
resto= entrada%2

if resto==0:
    par=1
else:
    impar=1

if entrada>0:
    positivo=1
elif entrada<0:
    negativo=1
    
if par==1 and positivo==1:
    print('POSITIVO PAR')
elif impar==1 and positivo==1:
    print("POSITIVO IMPAR")
elif par==1 and negativo==1:
    print("NEGATIVO PAR")
elif impar==1 and negativo==1:
    print("NEGATIVO IMPAR")

if entrada==0:
    print("NULO")