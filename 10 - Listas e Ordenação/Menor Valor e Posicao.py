quantidade=int(input())
valores=input().split()
lista=[int(i) for i in valores]
menorvalor=lista[0]
posicao=0
for n in lista:
    for p in range(quantidade):
        if n<menorvalor:
            menorvalor=n
            posicao=lista.index(n)
print("Menor valor:",menorvalor)
print("Posicao:",posicao)