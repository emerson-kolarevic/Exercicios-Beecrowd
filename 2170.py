X1, Y1 = map(int, input().split())
X2, Y2 = map(int, input().split())
X3, Y3 = map(int, input().split())

juros1 = ((Y1/X1)-1)*100
juros2 = ((Y2/X2)-1)*100
juros3 = ((Y3/X3)-1)*100

print("\nProjeto 1:")
print(f"Percentual dos juros da aplicacao: {juros1:.2f} %\n")

print("Projeto 2:")
print(f"Percentual dos juros da aplicacao: {juros2:.2f} %\n")

print("Projeto 3:")
print(f"Percentual dos juros da aplicacao: {juros3:.2f} %\n")
