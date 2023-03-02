posicao=input()
limiar=int(input())
matriz=int(input())
lista=[[int(i)for i in input().split()] for i in range (matriz)]

soma=0
if posicao=="acima":
    for linha in range(matriz-1):
        for coluna in range(linha+1,matriz):
            soma+=lista[linha][coluna]
else:
    for coluna in range(matriz-1):
        for linha in range(coluna+1,matriz):
            soma+=lista[linha][coluna]

if soma>limiar:
    print(True)
else:
    print(False)