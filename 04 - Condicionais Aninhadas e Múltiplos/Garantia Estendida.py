produto= float(input())
anos= int(input())
valorGarantia=0
total= valorGarantia+produto
if anos==2:
    valorGarantia= produto+(0.05*produto)
    print('%.2f'% (valorGarantia))
if anos==1:
    valorGarantia= produto+(0.03*produto)
    print('%.2f'% (valorGarantia))
if anos==0:
    print('%.2f'% produto)
