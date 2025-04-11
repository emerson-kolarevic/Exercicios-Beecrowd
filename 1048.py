reajuste1 = 15
reajuste2 = 12
reajuste3 = 10
reajuste4 = 7
reajuste5 = 4

salario = float(input())

if salario <= 400:
    n_salario = salario * (1 + (reajuste1/100))
    r_salario = n_salario - salario
    print(f"Novo salario: {n_salario:.2f}")
    print(f"Reajuste ganho: {r_salario:.2f}")
    print(f"Em percentual: {reajuste1} %")
elif salario > 400 and salario <= 800:
    n_salario = salario * (1 + (reajuste2/100))
    r_salario = n_salario - salario
    print(f"Novo salario: {n_salario:.2f}")
    print(f"Reajuste ganho: {r_salario:.2f}")
    print(f"Em percentual: {reajuste2} %")
elif salario > 800 and salario <= 1200:
    n_salario = salario * (1 + (reajuste3/100))
    r_salario = n_salario - salario
    print(f"Novo salario: {n_salario:.2f}")
    print(f"Reajuste ganho: {r_salario:.2f}")
    print(f"Em percentual: {reajuste3} %")
elif salario > 1200 and salario <= 2000:
    n_salario = salario * (1 + (reajuste4/100))
    r_salario = n_salario - salario
    print(f"Novo salario: {n_salario:.2f}")
    print(f"Reajuste ganho: {r_salario:.2f}")
    print(f"Em percentual: {reajuste4} %")
else: 
    n_salario = salario * (1 + (reajuste5/100))
    r_salario = n_salario - salario
    print(f"Novo salario: {n_salario:.2f}")
    print(f"Reajuste ganho: {r_salario:.2f}")
    print(f"Em percentual: {reajuste5} %")

# elif salario > 2000:
#     n_salario = salario * (1 + (reajuste5/100))
#     r_salario = n_salario - salario
#     print(f"Novo salario: {n_salario:.2f}")
#     print(f"Reajuste ganho: {r_salario:.2f}")
#     print(f"Em percentual: {reajuste5} %")