def parametro(nm):
    correcao={}
    if nm=='0':
        return
    for i in range(int(nm[0])):
        nomes=input().split('->')
        errado=nomes[0].strip()
        errado.strip()
        certo=nomes[1].strip()
        certo.strip()
        correcao[errado]=certo
    return correcao
'''
frase=[]
def Lista_frase():
    for i in range(int(nm[1])):
        entrada=input()
        frase.append(entrada)
'''   


def imprimir(correcao):
    frase_gg=[]
    for i in range(int(nm[1])):
        frase=input()
        for errado, certo in correcao.items():
            frase=frase.replace(errado,certo)
        frase_gg.append(frase)


    print('\n'.join(frase_gg))



while True:
    
    nm=input().split()
    if nm[0]=='0':
        break
    else:
        
        imprimir(parametro(nm))
    #nm=input().split()