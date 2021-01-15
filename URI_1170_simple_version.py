n = int(input())

for x in range(n):
    qtd = float(input())
    j = 0
    while(qtd > 1):
        qtd /= 2
        j += 1
    print(f'{j} dias')
