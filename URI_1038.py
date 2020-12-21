cod, q = map(int, input().split())
Item = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.5}

cod = float(Item[cod])*q

print(f'Total: R$ {cod:.2f}')
