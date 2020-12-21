vendedor = input()
salario = round(float(input()), 2)
vendas = round(float(input()), 2)

total = salario + (vendas*0.15)

# if(vendedor == vendedor.isupper):
print(f'TOTAL = R$ {total:.2f}')