salario= float(input())
if salario >500:
    salario= salario+(salario*0.1)
    print ('%.2f'%salario)
elif salario >300:
    salario= salario+(salario*0.07)
    print ('%.2f'% salario)
else:
    salario= salario+(salario*0.05)
    print ('%.2f'%salario)