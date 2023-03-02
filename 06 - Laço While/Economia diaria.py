entrada=float(input())
dindin=entrada
meta=0
dias=7
anterior=entrada
while dias>1:
    entrada=float(input())
    dindin+= entrada
    dias-=1
    if entrada>=anterior+0.5:
        meta+=1
    anterior=entrada
print("R$",'%.2f'%dindin)
print(meta)
