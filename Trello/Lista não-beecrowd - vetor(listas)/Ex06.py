lista = []
iguais_ou_acimamedia = []
abaixomedia = []

for i in range(6):
    valor = int(input(f"Digite um valor {i+1}: "))
    lista.append(valor)

media = sum(lista) / len(lista)

for i in lista:
    if i >= media:
        iguais_ou_acimamedia.append(i)
    else:
        abaixomedia.append(i)

print(f"\nA média dos valores digitados é: {media}")
print(f"\nOs números iguais e acima da média são: {iguais_ou_acimamedia}\n")
print(f"Os números abaixo da média são: {abaixomedia}\n")