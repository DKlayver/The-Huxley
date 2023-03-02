DadosP={}
total=Total=0
while True:
    idade=int(input())
    if idade==-1:
        break
    DadosP[idade]=input().split()
    if 18<=idade<=35 and DadosP[idade] == ['f','l','v']:
        total+=1
    Total+=1

print("Mais velho:",max(DadosP.items())[0])
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: %.2f"%(total/Total*100) + "%")