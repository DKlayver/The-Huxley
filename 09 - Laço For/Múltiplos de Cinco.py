entrada=input().split()
numero1=int(entrada[0])
numero2=int(entrada[1])
armazenamento=''
for cont in range(numero1, numero2+1):
    if cont%5==0:
        armazenamento=armazenamento+ str(cont)+ ' '
    

armazenamento= armazenamento.replace(' ','|')
print(armazenamento[:len (armazenamento)-1])