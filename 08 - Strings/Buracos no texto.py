repeticoes=int(input())

for cont in range(repeticoes):
    palavra=input().upper()
    soma=0
    for letra in palavra:
        if letra== "A" or letra== "D" or letra== "O" or letra== "P" or letra== "R" or letra== "Q":
            soma+=1
        elif letra=="B":
            soma=soma+2
    print(soma)