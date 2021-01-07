def mdc(f1, f2):
    resto = None
    while resto != 0:
        resto = f1 % f2
        f1 = f2
        f2 = resto
    return f1


n = int(input())

for i in range(n):
    numeros = [int(num) for num in input().strip().split()]
    print(mdc(numeros[0], numeros[1]))
