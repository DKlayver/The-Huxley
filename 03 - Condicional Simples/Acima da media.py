n1= float(input())
n2=float(input())
n3= float(input())
x1=0
x2=0
x3=0
media= (n1+n2+n3)/3
if n1>media:
    x1=1
if n2>media:
    x2=1
if n3>media:
    x3=1

if x1 and x2 ==1:
    print('2')
if x1 and x3 ==1:
    print('2')
if x2 and x3==1: 
    print ('2')

if x1 and x2 and x3 ==1:
    print('3')

if x1==1 and x2 !=1 and x3!=1:
    print('1')
if x1!=1 and x2 ==1 and x3!=1:
    print('1')
if x1!=1 and x2 !=1 and x3==1:
    print('1')
if x1!=1 and x2 !=1 and x3!=1:
    print('0')