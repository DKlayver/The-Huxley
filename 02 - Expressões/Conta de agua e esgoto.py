entrada= input()
valores= entrada.split()
m3gasto= float(valores[0])
custom3= float(valores[1])
esgoto= m3gasto*0.8
litros= m3gasto*1000
elitros= esgoto*1000
valoragua= litros*custom3
valoresgoto= elitros*custom3
print ('%.2f'% valoragua)
print ('%.2f'% valoresgoto)
print ('%.2f'% (valoragua+valoresgoto))