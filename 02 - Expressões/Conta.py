kwh= float(input())
VT= kwh*1.5
VC= VT-(VT*0.15)
print("Valor a ser pago: R$ "'%5.2f'% VT, "reais")
print("Valor a ser pago com desconto: R$ "'%5.2f'% VC, "reais")
