while True:
    try:
        a, b = map(int, input().split())

        soma = a ^ b
        print(soma)

    except EOFError:
        break
