dados={}
while True:
  passagem=int(input())
  if passagem==-1:
    break
  for i in range(4):
    input()
  poltrona=int(input())
  idade=int(input())
  nome=input()
  idade_poltrona=(idade,poltrona)
  dados[nome]=idade_poltrona

tupla=[]
idade_total=0
for nome,idade_poltrona in dados.items():
  idade_total+=idade_poltrona[0]
  tupla.append((nome,idade_poltrona))

idade_media=idade_total/(len(tupla))
for dado in tupla:
  if dado[1][0]>=idade_media and dado[1][1]%2==0:
    print(dado[0])