# Escreva um programa que, dado um vetor de números inteiros, 
# calcule a mediana dos elementos do vetor.

# Madiana total de elementos impar
import random

lista_impar = []

for i in range(9):
    valor1 = random.randrange(1,51)
    lista_impar.append(valor1)
    lista_impar.sort()

print(lista_impar)

mediana_lista_impar = (len(lista_impar) // 2)

print(f"A mediana da lista com total de elementos impar é {lista_impar[mediana_lista_impar]}\n")

lista_par = []

for i in range(10):
    valor2 = random.randrange(1,51)
    lista_par.append(valor2)
    lista_par.sort()

print(lista_par)

mediana_lista_par1 = lista_par[(len(lista_par) // 2)]
mediana_lista_par2 = lista_par[(len(lista_par) // 2 - 1)]

mediana = (mediana_lista_par1 + mediana_lista_par2) / 2

print(f"A mediana da lista com total de elementos par é {mediana}\n")