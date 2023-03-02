entrada=int(input())
valor=0
def taxa1(a):
    return (a-20)*2
def taxa2(a):
    return 160+(a-100)*5


while entrada>10:
    if entrada<31:
        print (entrada-10+7)
        break
    elif entrada<101:
        print(taxa1(entrada)+7)
        break
    elif entrada>=101:
        print(taxa2(entrada)+7)
        break
if entrada<=10:
    print('7')