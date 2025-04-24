P, R, N = map(float, input().split())
# p = valor emprestimo
# r = taxa de juros anual
# n = numero de prestações mensais

juros_mes = (R/100) / N

prestacao = P * (juros_mes / (1-(1 + juros_mes)**-N))

print(f"{prestacao:.6f}")