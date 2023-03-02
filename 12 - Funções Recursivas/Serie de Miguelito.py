lista=list('3')
def SerieMiguelito(lista):
    
    for i in range(50):
        lista.append(int(lista[-1])+4)
        lista.append(int(lista[-1])+1)
    return lista
SerieMiguelito(lista)

def Miguelito(entrada):
    if entrada==1:
        return (3)
    else:
        return lista[entrada-1]

entrada=int(input())
print(Miguelito(entrada))
