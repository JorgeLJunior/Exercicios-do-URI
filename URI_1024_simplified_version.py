linhas = int(input())

for i in range(linhas):
    msg = input()
    msg_new = ''

    for j in msg:
        if j.isalpha() == True:
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
