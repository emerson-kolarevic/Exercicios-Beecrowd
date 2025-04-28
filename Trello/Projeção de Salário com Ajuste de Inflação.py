import random

def menu ():
    print("1. Defina o salário inicial")
    print("2. Adicionar uma taxa de inflação")
    print("3. Preencher taxas inflação fixas")
    print("4. Preencher taxas inflação aleatórias")
    print("5. Excluir a última taxa de inflação inserida")
    print("6. Calcular e exibir valores de salario e inflação")
    print("7. Sair do programa")

lista_inflacao = []
salario_inicial = 0

while True:

    print("Escolha uma opção abaixo:\n")
    menu()
    escolha = int(input(f"\nDigite sua escolha: "))

    if escolha == 1:
        salario_inicial = float(input("Digite o salario: \n"))
        print("Escolha uma opção para continuar\n")
        

    elif escolha == 2:
        while True:
            inflacao_manual = float(input("Digite a inflação: "))
            lista_inflacao.append(inflacao_manual)
            continuacao = input("Deseja inserir mais dados (S/N)").lower()
            if continuacao == "n":
                break
       
    
    elif escolha == 3:
        inflacao_repetida = float(input("Qual a inflação: "))
        anos = int(input("Quantos anos para essa inflação: "))
        for i in range(anos):
            lista_inflacao.append(inflacao_repetida)
       
    
    elif escolha == 4:
        inflacao_aleatoria_min = float(input("Qual a inflação mínima no período: "))
        inflacao_aleatoria_max = float(input("Qual a inflação máxima no período: "))
        anos = int(input("Quantos anos para essa inflação: "))
        for i in range(anos):
            valor = random.uniform(inflacao_aleatoria_min,inflacao_aleatoria_max)
            valor = round(valor, 2)
            lista_inflacao.append(valor)
        print("Lista de inflação geradas:")
        print(lista_inflacao)
        
    
    elif escolha == 5:
        if len(lista_inflacao) == 0:
            print("Não há taxas de inflação para excluir")
        else:
            removido = lista_inflacao.pop()
            print(f"Última taxa de inflação removida: {removido:.2f}%")
        
    
    elif escolha == 6:
    
        if salario_inicial == 0:
            print("Valor do salário não informado")
        elif len(lista_inflacao) == 0:
            print("Lista de inflações vazia, adicione taxas primeiro")    
        else:
            salario_atual = salario_inicial
            acumulado = 1
            
            print("\nProjeção Salarial:")
            for ano, inflacao in enumerate(lista_inflacao, start=1):
                salario_atual *= (1 + inflacao / 100)
                acumulado *= (1 + inflacao / 100)

                print(f"Ano {ano}: Salário = R$ {salario_atual:.2f} (Inflação: {inflacao:.2f}%)")

                if inflacao > 10:
                    print(f"Aumento de inflação acima de 10% no ano {ano}!")
                
                if (acumulado -1) > 0.30:
                    print(f"Atenção: Inflação acumulada já ultrapassou 30% até o ano {ano}!")
                    
        taxa_acumulada = 100 * (acumulado - 1)
        print(f"\nInflação acumulada total após {len(lista_inflacao)} anos: {taxa_acumulada:.2f}%")
    
    
    elif escolha == 7:
        break

