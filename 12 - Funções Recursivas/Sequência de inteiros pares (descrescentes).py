def ParesDecescente(cont):
    if cont<0:
        return 1
    else:
        if cont%2==0:
            print(cont)
            return 1+ParesDecescente(cont-1)
            
        else:
            return ParesDecescente(cont-1)
cont=int(input())
ParesDecescente(cont)