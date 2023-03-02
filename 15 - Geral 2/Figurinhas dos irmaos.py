figurinhas=int(input())
dados={"maria":{},"joao":{}}
for x in range(figurinhas):
    n_serie=int(input())
    if n_serie%2:
        dados["joao"][n_serie]=dados["joao"].get(n_serie,0)+1
    else:
        dados["maria"][n_serie]=dados["maria"].get(n_serie,0)+1

lista_cont=[]
for pessoa,n_serie_quant in dados.items():
    cont=0
    lista_aux=[]
    for n_serie, quant in n_serie_quant.items():
        cont+=quant
        lista_aux.append(n_serie)
    lista_cont.append(lista_aux)
    print(cont)

if sum(lista_cont[0])>sum(lista_cont[1]):
    print(sum(lista_cont[0]))
else:
    print(sum(lista_cont[1]))