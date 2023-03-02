tamanho=int(input())
matriz=list()
#adicionando os valores � matriz
for n in range(tamanho):
    matriz.append(input().split())
#print (matriz)
# achando a diagonal principal
diagonalPrincipal=list()
for i in range(tamanho):
    diagonalPrincipal.append(matriz[i][i])
#print(diagonalPrincipal)
#invertendo a diagonal principal
diagonalPrincipal.reverse()
#substituindo a diagonal principal da matriz pela a inversa da mesma
for j in range(tamanho):
    matriz[j][j]=diagonalPrincipal[j]
#print(matriz)
#criando a diagonal secundaria
diagonalSecundaria=list()
for i in range(tamanho-1,-1,-1):
    diagonalSecundaria.append(matriz[tamanho-1-i][i])
#print(diagonalSecundaria)
#multiplicando a diagonal secundaria por 2
SecundariaX2=list()
for u in range(tamanho):
    SecundariaX2.append(str(int(diagonalSecundaria[u])*2))
#print(SecundariaX2)
#adicionando a diagonal secundaria na matriz
cont=0
for p in range(tamanho-1,-1,-1):
    matriz[tamanho-1-p][p]=SecundariaX2[tamanho-1-p]
    cont+=1
#print(matriz)
#achando a transposta da matriz
copia=list()
for r in range(tamanho):
    copia.append(matriz[r].copy())


for r in range(tamanho):
    for joj in range(r+1,tamanho):
        matriz[r][joj]=matriz[joj][r]
        

for r in range(tamanho):
    for joj in range(r+1,tamanho):
        matriz[joj][r]=copia[r][joj]

for r in matriz:
    print(' '.join(r)+' ')