entrada=int(input())
valores=[float(input()) for i in range(entrada)]
Acima=0
Abaixo=0
media=sum(valores)/len(valores)

for p in valores:
    if p>=media*1.1:
        Acima+=1
    elif p<=media*0.9:
        Abaixo+=1
print('%.2f'% media)
print(Acima)
print(Abaixo)