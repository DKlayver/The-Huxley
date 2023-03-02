livros= int(input())
alunos= int(input())

if alunos/livros <=8:
    print("A")
if alunos/livros <=12 and alunos/livros >=9:
    print("B")
if alunos/livros <=18 and alunos/livros >=13:
    print("C")
if alunos/livros >18:
    print("D")
