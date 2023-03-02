M=int(input())
N=int(input())                   

maior=0
contador=0
result=0
if N<M:
    print("sem multiplos menores que", N)
else:
    while M*contador<=N:
        result=M*contador
        contador=contador+1
    print(result)  