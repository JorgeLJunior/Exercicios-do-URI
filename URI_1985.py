p = int(input())
valor = []
cardapio = {1001: '1.50', 1002: '2.50', 1003: '3.50', 1004: '4.50', 1005: '5.50'}

if 1 <= p <= 5:
    codigo = []
    equal_var = list()

    for j in range(p):

        cod, q = map(int, input().split())
        codigo.append(cod)

        if 1 <= q <= 500:
            total = float(cardapio[cod]) * q
            valor.append(total)
            equal_var = list(set(codigo))

            if p > 2:
                if len(codigo) == len(equal_var):
                    continue
                else:
                    break
            else:
                if j > 0:
                    if codigo != equal_var:
                        break
                    else:
                        continue

    if not len(codigo) != len(equal_var):
        print(f'{sum(valor):.2f}')
    else:
        pass
