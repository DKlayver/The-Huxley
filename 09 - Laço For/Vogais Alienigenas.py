repeticoes=int(input())
for cont in range(repeticoes):
    soma=0
    vogais=input()
    texto=input()
    for letras in vogais:
        soma=int(texto.count(letras))+soma
        
    print(soma)
