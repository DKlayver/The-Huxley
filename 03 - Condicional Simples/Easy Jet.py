largura= float(input())
comprimento= float(input())
altura= float(input())
# 45 56 25
if largura > 45 or comprimento > 56 or altura > 25:
    print("PROIBIDA")

if largura <= 45 and comprimento <= 56 and altura <= 25:
    print("PERMITIDA")