produtos = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

x, y = map(int, input().split())

valor = produtos[x] * y

print(f"Total: R$ {valor:.2f}")