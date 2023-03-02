a=int(input()) 
b=int(input()) 
contador=0
menorV=0
maiorV=0
somatorio=0
if a<b: 
    menorV=a
    maiorV=b
else:
    menorV=b
    maiorV=a
if menorV<0:    
    menorV=0

while menorV<=maiorV:
    somatorio=menorV+(somatorio)
    menorV=menorV+1
print(somatorio)