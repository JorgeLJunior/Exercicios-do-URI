x, y = map(float, input().split())

if 0 == x == y:
    print(f'Origem')
if x > 0 and y == 0 or x < 0 and y == 0:
    print(f'Eixo X')
if y > 0 and x == 0 or y < 0 and x == 0:
    print(f'Eixo Y')
if x > 0 and y > 0:
    print(f'Q1')
elif x > 0 > y:
    print(f'Q4')
if x < 0 < y:
    print(f'Q2')
elif x < 0 and y < 0:
    print(f'Q3')
