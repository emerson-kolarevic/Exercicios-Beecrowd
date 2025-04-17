pendentes = ["1 - Estudar Inglês", "2 - Fazer Compras"]
andamento = ["1 - Apresentação Marketing"]
concluidas = []

print("\n-----Programa Iniciado-----\n")

print("Escolha uma opção no menu abaixo:\n")

print("1. Tarefas Pendentes")
print("2. Tarefas em Andamento")
print("3. Tarefas Concluídas")
print("4. Sair do Programa")

while True:
    opcao = int(input("\nDigite a opção desejada: "))
    if opcao == 1:
        if len(pendentes) == 0:
            print("Nenhuma tarefa pendente")
        else:
            for i in pendentes:
                print(i)
    elif opcao == 2:
        if len(andamento) == 0:
            print("Nenhuma tarefa em andamento")
        else:
            for i in andamento:
                print(i)
    elif opcao == 3:
        if len(concluidas) == 0:
            print("Nenhuma tarefa concluida")
        else:
            for i in concluidas:
                print(i)
    elif opcao == 4:
        print("\n----Programa Encerrado----\n")
        break
    else:
        print("\nOpção não disponível, digite novamente")


        
        
