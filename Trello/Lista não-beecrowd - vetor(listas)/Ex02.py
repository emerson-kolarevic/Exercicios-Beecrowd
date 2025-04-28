# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra
# o maior e o menor valor, sem usar as funções max, min e sort/sorted.

import random

lista = []

for i in range(10):
    valor = random.randrange(1,101)
    lista.append(valor)

print(lista)

maior = lista[0]
menor = lista[0]

for i in lista:
    if maior < i:
        maior = i

print(f"O maior numero da lista é {maior}")

for i in lista:
    if menor > i:
        menor = i

print(f"O menor numero da lista é {menor}")
    

