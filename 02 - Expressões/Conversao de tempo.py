t= int(input()) 
h=0
m=0
s=0

if t>= 3600:
    h= t//3600 
    t= t-h*3600 

if t>= 60:
    m= t//60 
    t= t-m*60 

s= t

print ("%d:%d:%d"%(h,m,s))