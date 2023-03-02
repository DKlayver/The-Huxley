lista=list()
tracinho=['-' for cont in range(50)]

while True:
    nome=input()
    if nome=='FIM':
        break
    lista.append(nome)

while True:
    lista.sort()
    print('\n'.join(lista))
    tamanho=int(input())
    if tamanho==0:
        break
    for cont in range(tamanho):
        lista.append(input())
    print(''.join(tracinho))