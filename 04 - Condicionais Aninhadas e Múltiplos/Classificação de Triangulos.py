A= int(input())
B= int(input())
C= int(input())

if A==B==C:
    print('equilatero')
elif A==B or A==C or B==C: 
    print('isosceles')
else:
    print('escaleno')
