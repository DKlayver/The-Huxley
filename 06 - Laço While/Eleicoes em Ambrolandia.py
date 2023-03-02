contAlibaba=0
contAlcapone=0
branco=0
nulo=0


entrada=int(input())
while entrada!=-1:
    
    if entrada==83:
        contAlibaba=contAlibaba+1
    elif entrada==93:
        contAlcapone=contAlcapone+1
    elif entrada==0:
        branco=branco+1
    elif entrada!=83 and entrada!=93:
        nulo=nulo+1
    entrada=int(input())


print(contAlibaba)
print(contAlcapone)
print(branco)
print(nulo)

if contAlibaba>contAlcapone:
    print("83")
else:
    print("93")

votosValidos= contAlcapone+contAlibaba+branco
percentAlibaba= (contAlibaba*100)/votosValidos
percentAlcapone=(contAlcapone*100)/votosValidos
print('%.2f' % percentAlibaba)
print('%.2f' % percentAlcapone)