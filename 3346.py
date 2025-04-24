ano_1, ano_2 = map(float,input().split())

acumulado = (((1+(ano_1/100)) * (1+(ano_2/100))) -1) * 100

print(f"{acumulado:.6f}")