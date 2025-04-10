a, b, c = map(float, input().split())

delta = b**2 - (4*a*c)

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    baskara1 = (-b + ((delta)**(1/2)))/(2*a)
    baskara2 = (-b - ((delta)**(1/2)))/(2*a)
    print(f"R1 = {baskara1:.5f}")
    print(f"R2 = {baskara2:.5f}")
