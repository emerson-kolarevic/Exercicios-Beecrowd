lista = []

contagem = 0

num1 = int(input())
lista.append(num1)

num2 = int(input())
lista.append(num2)

num3 = int(input())
lista.append(num3)

num4 = int(input())
lista.append(num4)

num5 = int(input())
lista.append(num5)

for i in lista:
    if i % 2 == 0:
        contagem += 1

print(f"{contagem} valores pares")