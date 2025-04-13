N = int(input())
teste = 1

while True:
    if teste > N:
        break

    A, B = map(int, input().split())
    
    strA = str(A)
    strB = str(B) 

    if len(strB) > len(strA):
        print("nao encaixa")
    else:
        if strA[-len(strB):] == strB:
            print("encaixa")
        else:
            print("nao encaixa")
                    
    teste += 1

