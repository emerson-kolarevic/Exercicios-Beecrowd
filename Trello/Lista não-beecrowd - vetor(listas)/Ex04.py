import random

lista = []

for i in range(10):
    valor = random.randrange(1,101)
    lista.append(valor)

lista_copia = lista.copy()

print(lista)
print(lista_copia)