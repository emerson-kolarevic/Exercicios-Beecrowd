# Escreva um programa em Python para verificar a nota do aluno em uma prova com 10
# questões, o programa deve perguntar ao aluno a resposta de cada questão e, após ele digitar
# as 10 respostas, comparar com o gabarito da prova e calcular o total de acertos e a nota
# (atribuir 1 ponto por resposta certa). 
# 
# Após um aluno digitar suas respostas, o programa deve
# perguntar se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido o
# programa deve informar:

# • O total de alunos que utilizaram o sistema;
# • A média das notas da turma;
# • O maior e a menor nota.

# Gabarito da Prova: 01 - A 02 - B 03 - C 04 - D 05 – E 06 - E 07 - D 08 - C 09 - B 10 - A



notas_alunos = []
gabarito = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "e", 7: "d", 8: "c", 9: "b", 10: "a"}
qtde_acertos = 0

while True:
    novo_aluno = input("Tem aluno para responder? (S/N): ").lower()
    if novo_aluno == "n":
        break

    for i in range(1,11):
        questao = input("Digite a resposta: ").lower()
        if gabarito[i] == questao:
            qtde_acertos += 1
    
    notas_alunos.append(qtde_acertos)
    
    qtde_acertos = 0

num_alunos = len(notas_alunos)
media_turma = sum(notas_alunos)/len(notas_alunos)
maximo = max(notas_alunos)
minimo = min(notas_alunos)

print(f"\n{num_alunos} alunos fizeram a prova")
print(f"\nA média da turma é {media_turma}")
print(f"\nA maior nota foi {maximo} e a menor nota foi {minimo}\n")
                       