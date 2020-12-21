a, b, c = map(int, input().split())

MAB = ((a + b) + abs(a - b)) / 2
MABC = ((MAB + c) + abs(MAB - c)) / 2

print(f'{MABC:.0f} eh o maior')
