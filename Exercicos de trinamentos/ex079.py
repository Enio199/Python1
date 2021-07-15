lista = []
while True:
    n = (int(input('digite um número ')))
    if n not in lista:
        lista.append(n)
        print(f'valor {n} adicionado a lista com sucesso')
    else:
        print(f'valor {n} já foi adicionado.')
    r = str(input('deseja coontinuar? [S/N]: ')).lower()
    if r == 'n':
        break
lista.sort()
print(f'Os valores digitado são {lista}')