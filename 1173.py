N = []

V = int(input())

while True:
    if V > 50:
        break
    else:
        N.append(V)
        for i in range(9):
            dobro = V * 2
            N.append(dobro)
            V = dobro

for i in range(10):
    print(f"N[{i}] = {N[i]}")
