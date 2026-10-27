"""
Dado {'a': 1, 'b': 2, 'c': 3}, crie outro dicionário com os valores ao quadrado.
"""
dicionario = {'a': 1, 'b': 2, 'c': 3}
novo_dicionario = dicionario.copy()

for chave, valor in novo_dicionario.items():
    novo_dicionario[chave] = valor ** 2

print(f'Dicionário original: {dicionario}')
print(f'Dicionário modificado: {novo_dicionario}')
