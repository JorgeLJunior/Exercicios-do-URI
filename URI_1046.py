hi, hf = list(map(int, input().split()))

if hi < hf:
    hora = hf - hi
else:
    hora = hf + 24 - hi

print(f'O JOGO DUROU {hora} HORA(S)')
