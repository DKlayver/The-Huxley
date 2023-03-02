entrada=input().upper()
sim=0
nao=0
nulo=0

while entrada!='ENCERRAR':
    if entrada=='SIM':
        sim+=1
    elif entrada=='NAO':
        nao+=1
    elif entrada=='NULO':
        nulo+=1
    entrada=input().upper()
if sim>(nao+nulo):
    print('COM FOGOS')
else:
    print('SEM FOGOS')