mes= int(input())
ano= int(input())
bisexto=0
impar= 0
numero=mes%2
div4= ano % 4
div100= ano % 100
div400= ano % 400

if div4 ==0 and div100!=0 or div400==0:
    bisexto=1
if div4!=0:
    bisexto=0
#bisexto qundo 1

if numero==0:
    impar=1
if numero!=0:
    impar=0
# 1 para paar 0 para impaar
if impar==1 and mes !=2 and mes!=8:
    print('30')

if impar==0 or mes==8:
    print('31')


if mes==2 and bisexto==0:
    print('28')
if mes==2 and bisexto==1:
    print('29')