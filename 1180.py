X = []
N = int(input())
X = list(map(int, input().split()))

menor = min(X)
posicao = X.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
