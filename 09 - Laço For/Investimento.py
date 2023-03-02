entrada=input().split()
investimento=float(entrada[0])
taxa=float(entrada[1])
anos=int(entrada[2])
meses=anos*12
trimestre=meses//3
montante=investimento

for cont in range(1, trimestre+1):
    rendimento=(montante*taxa)
    montante=float(investimento*(taxa+1)**cont)
    print('Rendimento:','%.2f' % rendimento,'Montante:','%.2f' % montante)