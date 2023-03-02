def velkmh(V0,A,T):
    V = V0 + A*T
    Vkmh = 3.6 * V
    return (Vkmh)

cont=3
menorV=0

while cont==3:
    V0=float(input())
    A=float(input())
    T=float(input())
    cont=cont-1
    menorV= velkmh(V0,A,T)
    
while cont==2:
    V0=float(input())
    A=float(input())
    T=float(input())
    cont=cont-1
    if velkmh(V0,A,T)<menorV:
        menorV= velkmh(V0,A,T)

while cont==1:
    V0=float(input())
    A=float(input())
    T=float(input())
    cont=cont-1
    if velkmh(V0,A,T)<menorV:
        menorV= velkmh(V0,A,T)
print(menorV)