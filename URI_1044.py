a, b, = map(int, input().split())

if b % a == 0 or a % b == 0:
    print(f'Sao Multiplos')
else:
    print(f'Nao sao Multiplos')
