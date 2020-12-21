cod1, num1, vu1 = input().split()
cod1 = int(cod1)
num1 = int(num1)
vu1 = float(vu1)

cod2, num2, vu2 = input().split()
cod2 = int(cod2)
num2 = int(num2)
vu2 = float(vu2)

total = num1 * vu1 + num2 * vu2

print(f'VALOR A PAGAR: R$ {total:.2f}')