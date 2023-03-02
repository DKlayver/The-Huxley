def verificar_primo(num):
  for cont in range(2,num):
    if num%cont==0:
      return False
  return True
  
valores=[int(i) for i in input().split()]
#3 5 7 11
total=1
for j in valores:
  if j<=1:
    total=False
    break
  elif verificar_primo(j):
    total*=j
  else:
    total=False
    break

if total==False:
  print("SEM PRODUTO")
else:
  print(total)