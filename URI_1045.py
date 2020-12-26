a, b, c = map(float, input().split())

if a > 0 and b > 0 and c > 0:
    lados = [a, b, c]
    lados.sort(key=float, reverse=True)
    a = max(lados)
    c = min(lados)
    b = lados[1]

    if a == b > c:
        b = a
    elif a > b <= c:
        b = c
    elif b < a > c < b:
        b = b

    if a >= b + c:
        print(f'NAO FORMA TRIANGULO')
    else:
        if a ** 2 == (b ** 2 + c ** 2):
            print(f'TRIANGULO RETANGULO')
        elif a ** 2 > (b ** 2 + c ** 2):
            print(f'TRIANGULO OBTUSANGULO')
        elif a ** 2 < (b ** 2 + c ** 2):
            print(f'TRIANGULO ACUTANGULO')
        if a == b and b == c and c == a:
            print(f'TRIANGULO EQUILATERO')
        elif a == b and b != c or b == c and c != a or c == a and a != b:
            print(f'TRIANGULO ISOSCELES')
