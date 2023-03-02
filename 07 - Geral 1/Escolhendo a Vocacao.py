For�a=int(input())
Inteligencia=int(input())
Destreza=int(input())
Furtividade=int(input())
Peso=int(input())

contador=25

while contador>0:
    if For�a>5 and Destreza>5 and Peso>5:
        print('Knight')
        break
    elif For�a<5 and Inteligencia>5 and Furtividade>5 and Peso<5:
        print('Mage')
        break
    elif For�a>5 and Inteligencia>5 and Destreza>5 and Furtividade>5 and Peso<5:
        print('Paladin')
        break
    elif For�a>10 and  Inteligencia<5 and Destreza<5 and Furtividade<5 and Peso>5:
        print('Orc')
        break 