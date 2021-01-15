renda = float(input())

if 0.00 <= renda <= 2000.00:
    print(f"Isento")

elif 2000.01 <= renda <= 3000.00:
    renda = renda - 2000.00
    renda_n = 0.08 * renda
    print(f'R$ {renda_n:.2f}')

elif 3000.01 <= renda <= 4500.00:
    renda1 = renda - 2000.00
    renda2 = renda - 3000.00
    renda_n = (0.08 * (renda1 - renda2)) + (renda2 * 0.18)
    print(f'R$ {renda_n:.2f}')

elif renda > 4500.00:
    renda1 = renda - 2000.00
    renda2 = renda - 3000.00
    renda3 = renda - 4500.00
    renda_n = (0.08 * (renda1 - renda2)) + ((renda2 - renda3) * 0.18) + (renda3 * 0.28)
    print(f'R$ {renda_n:.2f}')
