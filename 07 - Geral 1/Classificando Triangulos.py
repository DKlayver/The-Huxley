def tipo_triangulo(a,b,c):
    if  (abs(lado2-lado3)<lado1<(lado2+lado3))==False:
        print('INVALIDO')
    elif lado1==lado2 and lado2==lado3:
        print('EQUILATERO')
    elif lado1!=lado2!=lado3!=lado1:
        print('ESCALENO')
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print('ISOSCELES')

lados=input().split()
lado1=int(lados[0])
lado2=int(lados[1])
lado3=int(lados[2])

while lados!='FIM':
    tipo_triangulo(lado1,lado2,lado3)
    lados=input().split()
    try:
        lado1=int(lados[0])
        lado2=int(lados[1])
        lado3=int(lados[2])
    except:
        break