entrada= input()
valores= entrada.split()
A= float (valores[0])
B= float (valores[1])
C= float (valores[2])
pi = 3.14159
AT= (A*C)/2
AC= pi*(C**2)
ATR= (A+B)*C/2
AQ= B**2
AR= A*B
print("TRIANGULO: %.3f"% AT)
print("CIRCULO: %.3f" % AC)
print("TRAPEZIO: %.3f"% ATR)
print("QUADRADO: %.3f" % AQ)
print("RETANGULO: %.3f" % AR)