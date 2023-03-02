entrada= int(input())
numerador= 1
denominador= 3
#lista= (numerador+1)/(denominador+3)
contador=0
padrao=''
while contador<entrada:
    padrao= padrao+ str(numerador)+'/'+str(denominador)       
    numerador+=1
    denominador+=3
    contador+=1
    if contador!=entrada:
        padrao=padrao+' + '  
       
    
print(str(padrao))  
print('%.2f'%float(1/3*entrada))