vezes=int(input())
entrada=input().split()
lista=[int(i) for i in entrada]

entrada.reverse()
print(' '.join(entrada))
entrada.reverse()

primeiro=entrada[0]
entrada.pop(0)
entrada.append(primeiro)
print(' '.join(entrada))

lista.sort(reverse=True)
lista=[str(i) for i in lista]
print(' '.join(lista))