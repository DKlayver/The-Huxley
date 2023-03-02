lista= ' abcdefghijklmnopqrstuvwxyz'
while True:
    palavra=''
    codigo=input().split()
    for cont in codigo:
        palavra=palavra+lista[int(cont)]
    if palavra=='fim':
        break
    print(palavra)