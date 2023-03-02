lista=[input() for i in range(101)]

valor=lista[-1]
for p in range(100):
    if lista[p] == valor:
        print(p)