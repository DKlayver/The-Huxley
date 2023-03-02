dados={}
while True:
    entrada=input()
    if entrada=="FIM":
        break
    participante,amigo=entrada.split()
    dados[participante]=amigo

ListaDADOS=[]
amigo_ganho=''
for participante, amigo in dados.items():
    ListaDADOS.append((participante,amigo))
    if len(amigo_ganho) < len(participante) and amigo=="YES":
        amigo_ganho=participante

for i in range(len(ListaDADOS)-1,0,-1):
    for j in range(i):
        if ListaDADOS[j][1] < ListaDADOS[j+1][1]:
            ListaDADOS[j],ListaDADOS[j+1]=ListaDADOS[j+1],ListaDADOS[j]
        if ListaDADOS[j][0] > ListaDADOS[j+1][0] and ListaDADOS[j][1] == ListaDADOS[j+1][1]:
            ListaDADOS[j],ListaDADOS[j+1]=ListaDADOS[j+1],ListaDADOS[j]
 
for dado in ListaDADOS:
    print(dado[0])
print()
print("Amigo do Habay:\n"+amigo_ganho)