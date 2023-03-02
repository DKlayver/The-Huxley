def AnalisarSituacao(media):
    if media>=9:
        print ("aprovado com louvor")
    elif media>=7:
        print ("aprovado")
    elif media <3:
        print ("reprovado")
    elif 7>media>=3:
        print("prova final")
    
valores=input().split()
a,b,c,d= float(valores[0]), float(valores[1]), float(valores[2]), float(valores[3])
media= float(a*1+b*2+c*3+d*4)/10

AnalisarSituacao(media)