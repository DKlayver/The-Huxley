media= float(input())
faltas= int(input())
if faltas>10:
    print("REPROVADO POR FALTAS")
elif media<7:
    print("REPROVADO")
elif 9.5>media>=7:
    print("APROVADO")
elif 9.5<=media:
    print("APROVADO COM LOUVOR")
