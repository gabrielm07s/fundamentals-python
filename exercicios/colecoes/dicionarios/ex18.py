"""
Dados dois dicionários, mostre as chaves em comum e as chaves exclusivas de cada um.
"""
dicionario1 = {'a': 1, 'b': 10, 'c': 3}
dicionario2 = {'d': 1, 'e': 10, 'c': 3}

chaves_dicionario1 = dicionario1.keys()
chaves_dicionario2 = dicionario2.keys()

print(f'Chaves em comum: {chaves_dicionario1 & chaves_dicionario2}')
print(f'Chaves exclusivas do D1: {chaves_dicionario1 - chaves_dicionario2}')
print(f'Chaves exclusivas do D2: {chaves_dicionario2 - chaves_dicionario1}')