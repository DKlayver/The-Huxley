entrada=float(input())

while entrada>2000:
    if entrada<=3000:
        print('R$ ' '%.2f' % (0.08*(entrada-2000)))
        break
    elif entrada<=4500:
        print('R$ ' '%.2f' % (0.18*(entrada-3000)+80))
        break
    elif entrada >4500:
        print('R$ ' '%.2f' % (0.28*(entrada-4500)+270+80))
        break
else:
    print('Isento')