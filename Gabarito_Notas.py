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
print(f"\n{num_alunos} alunos fizeram a prova")
print(f"\nA média da turma é {media_turma}")
                       