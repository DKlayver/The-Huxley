dias= int(input())
quilometros= int(input())
diaria= dias*90
limite= dias*100
kmexcedido=(quilometros-limite)
valor= kmexcedido*12
total=0
        
if quilometros>limite:
    total= ('%.2f'% (diaria + valor))
    print (total)

if quilometros<=limite:
    total= ('%.2f'% diaria)
    print (total)
