import math

while True:
    try:
        entrada = input()
        if not entrada:
            break
        
        D, VF, VG = map(int, entrada.split())
        
        # Se a Guarda for mais lenta, nem precisa calcular
        if VG <= VF:
            print('N')
            continue
        
        tempo_fugitivo = 12 / VF
        tempo_guarda = math.sqrt(D**2 + 12**2) / VG

        if tempo_guarda <= tempo_fugitivo:
            print('S')
        else:
            print('N')
            
    except EOFError:
        break