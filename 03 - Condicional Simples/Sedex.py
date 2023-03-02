diametro= int(input())
dimensoes= input()

valores= dimensoes.split()

largura=int(valores[0])
altura=int(valores[1])
profundidade=int(valores[2])

if diametro <= largura and diametro <= altura and diametro <= profundidade:
    print ("S")

if diametro > largura or diametro > altura or diametro > profundidade:
    print ("N")
