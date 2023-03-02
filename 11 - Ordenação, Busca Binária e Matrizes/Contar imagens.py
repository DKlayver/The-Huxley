def consultar_matriz():
    entrada = input().split()
    linhas = int(entrada[0])
    colunas = int(entrada[1])

    matriz = []
    for i in range(linhas):
        numeros = input().split()
        matriz.append(numeros)
    return matriz

def imagem(matriz1, matriz2, i, u):
    for lin in range(len(matriz2)):
        for col in range(len(matriz2[0])):
            if matriz2[lin][col] != matriz1[lin+i][col+u]: 
               return False
    return True

matriz = consultar_matriz()
matrizImagem = consultar_matriz()
 
contador = 0
for i in range(len(matriz)-len(matrizImagem) + 1):
    for j in range(len(matriz[0]) - len(matrizImagem[0]) + 1):
        if imagem(matriz, matrizImagem, i, j):
           contador += 1 

print(contador)