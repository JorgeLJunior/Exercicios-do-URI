d = int(input())

a = d // 365
d = d - (a * 365)

m = d // 30
d = d - (m * 30)

di = d
print(f'{a} ano(s)\n{m} mes(es)\n{di} dia(s)')
