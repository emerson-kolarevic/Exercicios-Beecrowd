par = []
impar = []

for i in range(15):
    valor = int(input())
    
    if valor % 2 == 0:
        par.append(valor)
        if len(par) == 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par.clear()
    else:
        impar.append(valor)
        if len(impar) == 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
