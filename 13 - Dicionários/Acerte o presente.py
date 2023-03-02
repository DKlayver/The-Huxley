quantidade=int(input())
pessoas_presentes={}
for i in range(quantidade):
    nomes_presentes=input().split()
    pessoas_presentes[nomes_presentes[0]]=nomes_presentes[1],nomes_presentes[2],nomes_presentes[3]

while True:
    entrada=input().split()
    if entrada[0]=='FIM':
        break
    else:
        if entrada[0] not in pessoas_presentes:
            print('Tente Novamente!')
        elif entrada[0] in pessoas_presentes:
            if entrada[1] in pessoas_presentes[entrada[0]]:
                print('Uhul! Seu amigo secreto vai adorar')
            else:
                print('Tente Novamente!')