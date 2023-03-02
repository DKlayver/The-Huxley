while True: 
  camisas=int(input())
  if camisas==0:
    break
  dados={}
  for i in range(camisas):
    aluno=input()
    dados[aluno]=input().split()
  lista=list()
  for aluno, cor_tamanho in dados.items():
    lista.append((cor_tamanho[0],cor_tamanho[1],aluno))

  for i in range(len(lista)-1,0,-1):
    for j in range(i):
      if lista[j][0]>lista[j+1][0]:
        lista[j],lista[j+1]=lista[j+1],lista[j]
      if lista[j][1]<lista[j+1][1] and lista[j][0]==lista[j+1][0]:
        lista[j],lista[j+1]=lista[j+1],lista[j]
      if lista[j][2]>lista[j+1][2] and lista[j][0]==lista[j+1][0] and lista[j][1]==lista[j+1][1]:
        lista[j],lista[j+1]=lista[j+1],lista[j]

  for dado in lista:
    print(" ".join(dado))
  print()