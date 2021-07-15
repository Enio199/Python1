nome = str(input('digite uma frase: ')).strip().lower()
print(f'A letra A aprace {nome.count("a")} vezes na frase')
print(f'A letra A aparece a primeira vez na posição {nome.find("a"[0]) + 1}')
print(f'A letra "A" aparece pela última vez na posição {nome.rfind("a") + 1}')