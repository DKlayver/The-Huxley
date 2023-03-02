def maiorAB(y,z):
    return((y+z+abs(y-z))//2)
    
entrada=input()
A,B,C= entrada.split()
A= int(A)
B= int(B)
C= int(C)
X= maiorAB(A,B)
print (maiorAB(X,C), "eh o maior")