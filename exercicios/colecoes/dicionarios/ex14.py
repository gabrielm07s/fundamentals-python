"""
Dada uma lista de números, crie {'pares': [...], 'impares': [...]}.
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

dicionario_numeros = {'pares': [], 'impares': []}

for n in numeros:
    if n % 2 == 0:
        dicionario_numeros['pares'].append(n)
    else:
        dicionario_numeros['impares'].append(n)

print(dicionario_numeros)