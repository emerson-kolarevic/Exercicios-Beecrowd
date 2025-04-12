x, y = map(int, input().split())
l1, h1 = map(int, input().split())
l2, h2 = map(int, input().split())

def cabe(x, y, l1, h1, l2, h2):
    # lado a lado
    if(l1 + l2 <= x and max(h1, h2) <= y):
        return True
    # Empilhadas
    if(h1 + h2 <= y and max(l1, l2) <= x):
        return True
    return False

# Testando todas as rotações possíveis das fotos
resultado = (
    cabe(x, y, l1, h1, l2, h2) or
    cabe(x, y, h1, l1, l2, h2) or
    cabe(x, y, l1, h1, h2, l2) or
    cabe(x, y, h1, l1, h2, l2)
)

# Impriome resposta
print("S" if resultado else "N")