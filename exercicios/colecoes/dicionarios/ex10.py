"""
Junte dois dicionários num terceiro (update e depois {**d1, **d2}) e veja o que acontece com chaves repetidas.
"""
dicionario1 = {'a': 1, 'b': 2, 'e': 5}
dicionario2 = {'c': 4, 'd': 5, 'e': 6}
dicionario3 = {**dicionario1, **dicionario2}

print(f'Dicionário 1: {dicionario1}')
print(f'Dicionário 2: {dicionario2}')
print(f'Dicionário 3: {dicionario3}')
