valor_eua=float(input()) #3.8l
valor_br=float(input()) #1l
cota=float(input())
litroeua=0

def litroemreal(valor_eua, cota):
    return float((valor_eua/3.8)*cota)

print('Gasolina EUA: R$ ''%.2f'% litroemreal(valor_eua,cota))
print('Gasolina Brasil: R$ ''%.2f' % valor_br)

if litroemreal(valor_eua, cota)>valor_br:
    print ('Mais barata no Brasil')
elif litroemreal(valor_eua, cota)<valor_br:
    print('Mais barata nos EUA')
elif litroemreal(valor_eua, cota)==valor_br:
    print('Igual')