N = int(input())
contagem = 1

while contagem <= 10000:
    if contagem % N == 2:
        print(contagem)
        contagem += 1
    else:
        contagem += 1