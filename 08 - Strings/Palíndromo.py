repeticoes=int(input())


for cont in range(repeticoes):
    texto=input().upper()
    texto=texto.replace(' ','')
    textoivertido=texto[::-1]
    if texto==textoivertido:
        print('SIM')
    else:
        print('NAO')