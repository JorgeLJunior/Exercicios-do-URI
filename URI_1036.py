from math import sqrt, pow

a, b, c = map(float, input().split())


d = 2 * a
delta = (pow(b, 2)) - (4 * a * c)

if a == 0 or a < 0 or c < 0 or d == 0 or delta < 0:
    print(f'Impossivel calcular')
else:
    r1 = (- b + sqrt(delta)) / d
    r2 = (- b - sqrt(delta)) / d
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
