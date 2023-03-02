DadosPaises={}
while True:
  entrada=input()
  if entrada=='*':
    break
  pais,medalha=entrada.split(',')
  if pais not in DadosPaises:
    DadosPaises[pais]={}
    for medalha2 in ["ouro","prata","bronze"]:
      if medalha2 not in DadosPaises[pais]:
        DadosPaises[pais][medalha2]=0
  DadosPaises[pais][medalha]=DadosPaises[pais].get(medalha,0) +1
 
ListaDados=list()
for pais, medalha_quantmedalha in DadosPaises.items():
  lista_aux=[]
  for medalha, quantmedalha in medalha_quantmedalha.items():
    lista_aux.append(quantmedalha) 
  ListaDados.append((pais,lista_aux[0],lista_aux[1],lista_aux[2])) 

for i in range(len(ListaDados)-1,0,-1):
  for j in range(i):
    if ListaDados[j][1]<ListaDados[j+1][1]:
      ListaDados[j],ListaDados[j+1]=ListaDados[j+1],ListaDados[j]
    if ListaDados[j][2]<ListaDados[j+1][2] and ListaDados[j][1]<=ListaDados[j+1][1]:
      ListaDados[j],ListaDados[j+1]=ListaDados[j+1],ListaDados[j]
    if ListaDados[j][3]<ListaDados[j+1][3] and ListaDados[j][2]<=ListaDados[j+1][2] and ListaDados[j][1]<=ListaDados[j+1][1]:
      ListaDados[j],ListaDados[j+1]=ListaDados[j+1],ListaDados[j]

cont=0
for dado in ListaDados:
  cont+=1
  print("%d)%s ouro:%d prata:%d bronze:%d"%(cont,dado[0],dado[1],dado[2],dado[3]))