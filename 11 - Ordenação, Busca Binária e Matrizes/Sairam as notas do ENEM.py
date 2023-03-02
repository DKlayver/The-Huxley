def busca_binaria(lista,valor):
    primeiro=0
    ultimo=len(lista)-1

    while primeiro<= ultimo:
        meio = (primeiro + ultimo)//2
        if lista[meio]==valor:
            return meio
        else:
            if valor<lista[meio]:
                ultimo=meio-1
            else:
                primeiro=meio+1
    return -1

pessoas=int(input())
cpf=[int(input()) for i in range(pessoas)]
notas=[int(input())for i in range(pessoas)]
NumeroTestes=int(input())
testes=[int(input())for i in range(NumeroTestes)]

for i in testes:
    posicao=busca_binaria(cpf,i)
    if posicao!=-1:
        print(notas[posicao])
    else:
        print("NAO SE APRESENTOU")