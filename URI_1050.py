num = int(input())
contato = {61: 'Brasilia', 71: 'Salvador', 11: 'Sao Paulo', 21: 'Rio de Janeiro',
           32: 'Juiz de Fora', 19: 'Campinas', 27: 'Vitoria', 31: 'Belo Horizonte'}

cidade = contato.get(num)  # Evita retornar na saida o KeyError (.get() em um dict)

if cidade:
    print(cidade)
else:
    print(f"DDD nao cadastrado")
