A= int(input())
B=int(input())
C=int(input())

if B!=A!=C:
    print("A")
elif A!=B!=C:
    print("B")
elif B!=C!=A:
    print("C")
elif A==B==C:
    print("*")