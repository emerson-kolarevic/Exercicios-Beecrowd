while True:
    h1, m1, h2, m2 = map(int, input().split())

    if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
        break

    inicio = (h1 * 60) + m1
    fim = (h2 * 60) + m2

    if fim > inicio:
        print(fim - inicio)
    elif fim < inicio:
        print((24 * 60 - inicio) + fim)
    else:
        print(24 * 60)


# h1, m1, h2, m2 = map(int, input().split())
# inicio = (h1 * 60) + m1
# fim = (h2 * 60) + m2

# if fim > inicio:
#     print(fim - inicio)
# elif fim < inicio:
#     ajuste_fim = ((24 * 60) + (h2 * 60)) + m2
#     print(ajuste_fim - inicio)
# elif fim == inicio:
#     print("")