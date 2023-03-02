entrada=float(input())

if 25>=entrada>0:
    print('Intervalo [0,25]')
elif 50>=entrada>25:
    print('Intervalo (25,50]')
elif 75>=entrada>50:
    print('Intervalo (50,75]')
elif 100>=entrada>75:
    print('Intervalo (75,100]')
elif entrada>100 or entrada<0:
    print('Fora de intervalo')