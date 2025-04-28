# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [1,20,3,40,5,60,7,80,9,100]
lista3 = lista1.copy()

for indice in lista2:
    if indice not in lista3:
        lista3.append(indice)

print(lista3)
