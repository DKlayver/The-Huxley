
def ContaDigitospares(entrada):
    if len(entrada)==1:
        if int(entrada)%2==0:
            return 1
        else:
            return 0
    else:
        if int(entrada[0])%2==0:
            return ContaDigitospares(entrada[1:])+1
        else:
            return ContaDigitospares(entrada[1:])


entrada=input()
print(ContaDigitospares(entrada))