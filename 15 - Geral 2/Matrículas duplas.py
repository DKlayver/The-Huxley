ProgII=[i for i in input().split()]
ProgIII=[i for i in input().split()]
lista_alunos_dupla=[]
for aluno in ProgII:
    if aluno in ProgIII:
        lista_alunos_dupla.append(aluno)

print(" ".join(lista_alunos_dupla))