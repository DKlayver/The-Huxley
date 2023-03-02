tamanho=int(input())
matriz=[[int(i)for i in input().split()]for u in range(tamanho)]

coluna=linha=sair=coluna_anterior=linha_anterior=0
while True:
    if tamanho-1==coluna==linha:
        print('OK')
        break
    elif coluna==tamanho-1 and linha!=tamanho-1 and not(sair):
        if matriz[linha][coluna] and matriz[linha+1][coluna] and linha_anterior!=linha+1:
            linha_anterior=linha
            linha+=1
            coluna_anterior=500
        elif matriz[linha][coluna] and matriz[linha][coluna-1] and coluna-1!=coluna_anterior:
            coluna_anterior=coluna
            coluna-=1
            linha_anterior=500
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and linha_anterior!=linha-1:
            linha_anterior=linha
            linha-=1
        else:
            sair=1
    elif linha==tamanho-1 and coluna!=tamanho-1 and not(sair):
        if matriz[linha][coluna] and matriz[linha][coluna+1] and coluna+1!=coluna_anterior:
            coluna_anterior=coluna
            coluna+=1
            linha_anterior=500
        elif matriz[linha][coluna] and matriz[linha][coluna-1] and coluna-1!=coluna_anterior:
            coluna_anterior=coluna
            coluna-=1
            linha_anterior=500
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and linha_anterior!=linha-1:
            linha_anterior=linha
            linha-=1
        else:
            sair=1
    elif coluna!=0 and not(sair):
        if matriz[linha][coluna] and matriz[linha+1][coluna] and linha_anterior!=linha+1:
            linha_anterior=linha
            linha+=1
            coluna_anterior=500
        elif matriz[linha][coluna] and matriz[linha][coluna+1] and coluna+1!=coluna_anterior:
            coluna_anterior=coluna
            coluna+=1
            linha_anterior=500
        elif matriz[linha][coluna] and matriz[linha][coluna-1] and coluna-1!=coluna_anterior:
            coluna_anterior=coluna
            coluna-=1
            linha_anterior=500
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and linha_anterior!=linha-1:
            linha_anterior=linha
            linha-=1
        else:
            sair=1
    elif coluna==0 and not(sair):
        if matriz[linha][coluna] and matriz[linha+1][coluna]and linha_anterior!=linha+1:
            linha_anterior=linha
            linha+=1
            coluna_anterior=500
        elif matriz[linha][coluna] and matriz[linha][coluna+1] and coluna+1!=coluna_anterior:
            coluna_anterior=coluna
            coluna+=1
        elif matriz[linha][coluna] and matriz[linha-1][coluna] and linha_anterior!=linha-1:
            linha_anterior=linha
            linha-=1
        else:
            sair=1
    else:
        print('NOT OK')
        break