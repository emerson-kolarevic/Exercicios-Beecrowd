# A JBS, maior empresa de alimentos do mundo, está precisando de um sistema para calcular o
# aumento salarial anual de seus funcionários. O processo de cálculo de aumento salarial é um
# pouco complexo e segue as seguintes regras:

# 1. O aumento só será aplicado para funcionários que recebem pelo menos R$1000,00.
# 2. No primeiro ano, o percentual de aumento será de 1,5%.
# 3. A partir do segundo ano, os aumentos salariais serão progressivos, com um acréscimo de
# 10% sobre o percentual do aumento anterior.

# A JBS quer sua ajuda para calcular o salário atual de um funcionário com base em seu salário
# inicial e ano de contratação, levando em consideração o ano atual do sistema.

# O programa deve permitir que o usuário insira o salário inicial e o ano de contratação do funcionário, garantindo
# que os dados estejam dentro dos seguintes critérios:

# • O salário inicial deve ser maior ou igual a R$ 1.000,00.
# • O ano de contratação deve estar entre 1995 e o ano atual do sistema.
# • O programa deve, então, calcular o salário atual do funcionário com base nas informações
# fornecidas e nas regras de aumento salarial da JBS. 
# 
# Por fim, ele deve exibir o salário atual do funcionário e quantos % de aumento ele teve em relação ao salário inicial.

ano_atual = 2025

while True:
    ano_contratacao = int(input("Qual foi o ano de contratação: "))
    salario_contratacao = int(input("Qual o salário na contratação: "))

    if ano_contratacao < 1995:
        print("\nO ano de contratação foi antes de 1995. Não há aumento salarial.\n")
    elif salario_contratacao < 1000:
        print("\nO salário da contratação está abaixo de R$ 1.000,00. Não há aumento salarial.\n")
    else:
        anos_trabalho = ano_atual - ano_contratacao
        ajuste_primeiro_ano = 1.035
        ajuste_demais_anos = 1.10

        salario_primeiro_atualizacao = (salario_contratacao*ajuste_primeiro_ano)
        salario_atual = salario_primeiro_atualizacao * ((ajuste_demais_anos)**(anos_trabalho - 1))
        percentual_aumento = ((salario_atual / salario_contratacao)-1)*100

        print(f"\nO salário atual do funcionário é R$ {salario_atual:.2f}.")
        print(f"\nIsso corresponde a um aumento de {percentual_aumento:.2f}% em relação ao salário inicial de R$ {salario_contratacao:.2f}.")

    continuar = input("Deseja avaliar outro funcionário? (S/N): ").lower()

    if continuar != "s":
        print("\nEncerrando o programa. Até a próxima!")
        break


