aa, ll = map(int, input().split())
l1, a1 = map(int, input().split())
a2, l2 = map(int, input().split())

if a1 + a2 <=aa:
    if l1 <= ll:
        if l2 <= ll:
            print("S")
else:
    print("N")