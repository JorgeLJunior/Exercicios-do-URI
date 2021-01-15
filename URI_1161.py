from math import factorial

while True:
    try:
        m, n = map(int, input().split())

        m = factorial(m)
        n = factorial(n)

        print(m + n)

    except EOFError:
        break
