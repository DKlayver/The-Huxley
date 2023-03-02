a=int(input())
b=int(input())
c=int(input())
maior = menor = a

if maior<b:
    maior=b
if maior<c:
    maior=c
if menor>b:
    menor=b
if menor>c:
    menor=c
medio=a+b+c-maior-menor
print(medio)