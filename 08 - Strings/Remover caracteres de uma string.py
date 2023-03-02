palavra=input()
letras=input()

for cont in letras:
    palavra=palavra.replace(cont,'')
print(palavra)