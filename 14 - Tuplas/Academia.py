dados={}
for x in range(100):
  nome=input()
  if nome=="SAIR":
    break
  senha=input()
  mensalidade=input()
  dados[senha]=(nome,mensalidade)

while True:
  teste=input()
  if teste=='-1':
    break
  if teste in dados:
    (nome,mensalidade)=dados[teste]
    if mensalidade=='P':
      print(nome+", seja bem-vindo(a)!")
    else:
      print("N�o est� esquecendo de algo,",nome+"? Procure a recep��o!")
  else:
    print("Seja bem-vindo(a)! Procure a recep��o!")