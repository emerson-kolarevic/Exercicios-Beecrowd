i = 1

while True:
    try:
       X1, Y1 = map(float, input().split())

       juros = ((Y1/X1)-1)*100

       print(f"Projeto {i}:")
       print(f"Percentual dos juros da aplicacao: {juros:.2f} %\n")

    except EOFError:
        break
