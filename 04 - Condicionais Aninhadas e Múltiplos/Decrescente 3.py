A= int(input())
B= int(input())
C= int(input())

if B>A:
    B,A=A,B

if C>B:
    C,B=B,C

if B>A:
    B,A=A,B

print(A)
print(B)
print(C)    