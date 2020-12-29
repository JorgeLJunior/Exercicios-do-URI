import re
# re --> importa a biblioteca de expressões regulares (regex)
linhas = int(input())

for i in range(linhas):
    msg = str(input())
    msg_new = ''

    for j in msg:
        # Se o string presente em j for compativel com os padrões alfabeticos(alpha) a-z e A-Z, os caracteres serão deslocados 3 posições à direita.
        if re.match('[a-zA-Z]', j):
            msg_new += chr(ord(j) + 3)
        else:
            msg_new += j

    msg_new = msg_new[::-1]  # inversão da mensagem.
    half = int(len(msg_new) / 2)
    hf1 = msg_new[:half]
    hf2 = msg_new[half:]
    half_new = ''

    for x in hf2:
        half_new += chr(ord(x) - 1)

    print(hf1 + half_new)
