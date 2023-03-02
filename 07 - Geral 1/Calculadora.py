valor1=0
valor2=0
operador=''
memoria=0


while valor1!='&' or valor2!='&' or operador!='&':
    try:
        valor1=float(input())
        valor2=float(input())
    except:
        break
    operador=input()
    if operador=='+':
        memoria=valor1+valor2
        print('%.3f'% memoria)
    elif operador=='-':
        memoria=valor1-valor2
        print('%.3f'% memoria)
    elif operador=='*':
        memoria=valor1*valor2
        print('%.3f'% memoria)
    elif operador=='/':
        memoria=valor1/valor2
        print('%.3f'% memoria)

    while valor1!='&' or operador!='&':
        try:
            valor1=float(input())
            operador=input()
        except:
            break
        try:
            if operador=='+':
                memoria=memoria+valor1
                print('%.3f'% memoria)
            elif operador=='-':
                memoria=memoria-valor1
                print('%.3f'% memoria)
            elif operador=='*':
                memoria=memoria*valor1
                print('%.3f'% memoria)
            elif operador=='/':
                memoria=memoria/valor1
                print('%.3f'% memoria)
        except:
            print('operacao nao pode ser realizada')