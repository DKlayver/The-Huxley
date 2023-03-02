Voo_Lugares={}
def Voos_Vagas(Voo_Lugares):
    for i in range(37):
        entrada=input().split()
        if entrada[0]=='9999':
            return Voo_Lugares
        else:
            Voo_Lugares[entrada[0]]=int(entrada[1])

def Clientes(Voo_Lugares):
    Reservas={}
    while True:
        identidade_Voo=input().split()
        if identidade_Voo[0]=='9999':
            break
        else:
            Reservas[identidade_Voo[0]]=identidade_Voo[1]
            if identidade_Voo[1] in Voo_Lugares:
                if Voo_Lugares[identidade_Voo[1]]>0:
                    print(identidade_Voo[0])
                    Voo_Lugares[identidade_Voo[1]]-=1
                else:
                    print('INDISPONIVEL')
            else:
                print('INDISPONIVEL')


Voos_Vagas(Voo_Lugares)
Clientes(Voo_Lugares)
