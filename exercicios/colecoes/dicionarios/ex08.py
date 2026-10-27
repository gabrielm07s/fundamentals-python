"""
Mostre a chave associada ao maior valor.
"""
dicionario = {'a': 1, 'b': 10, 'c': 3}

valor_maior = max(dicionario.values())

for chave, valor in dicionario.items():
    if valor == valor_maior:
        chave_maior = chave
        break

print(f'Chave: {chave_maior}, Valor: {valor_maior}')