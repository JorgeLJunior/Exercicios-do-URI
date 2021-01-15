# Versão Utilizando arrays

def blobs(comida):
    val = []
    while int(comida) > 0:
        comida /= 2
        val.append(comida)

    return val


n = int(input())

for j in range(n):
    qtd = float(input())
    print(f'{len(blobs(qtd))} dias')
