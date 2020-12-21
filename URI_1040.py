n1, n2, n3, n4 = map(float, input().split())

media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4) / 10

print(f'Media: {media:.1f}')

if media >= 7.0:
    print(f'Aluno aprovado.')
if media < 5.0:
    print(f'Aluno reprovado.')
if 5.0 <= media <= 6.9:
    print(f'Aluno em exame.')
    ne = float(input())
    print(f'Nota do exame: {ne}')
    mf = (ne + media) / 2
    if mf >= 5.0:
        print(f'Aluno aprovado.\nMedia final: {mf}')
    elif mf <= 4.9:
        print(f'Aluno reprovado.')
