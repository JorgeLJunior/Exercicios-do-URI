x = float(input())
x = x + 0.001

if 0 <= x <= 1000000.00:
    valores = [100, 50, 20, 10, 5, 2]
    moedas = [1.0, .5, .25, .10, .05, .01]

    print('NOTAS:')

    for i in valores:
        valores = x // i
        print(f'{int(valores)} nota(s) de R$ {i:.2f}')
        x %= i

    print('MOEDAS:')

    for i in moedas:
        moedas = x // i
        print(f'{int(moedas)} moeda(s) de R$ {i:.2f}')
        x %= i
