def Analise(sudoku,coluna):
    for y in range(9):
        for z in range(1,10):
            repeticoesLinhas=sudoku[y].count(str(z))
            if repeticoesLinhas!=1:
                return('NAO')
    for y in range(9):
        for z in range(1,10):
            repeticoesColunas=coluna[y].count(str(z))
            if repeticoesColunas!=1:
                return('NAO')
    return('SIM')
 
entrada=int(input())

for z in range(entrada):
    sudoku=list()

    for y in range(9):
        sudoku.append(input().split())

    coluna=list()
    for n in range(9):
        lista_aux=list()
        for j in range(9):  
            lista_aux.append(sudoku[j][n])
        coluna.append(lista_aux)
    print('Instancia',z+1)
    print(Analise(sudoku,coluna)+'\n')