"""
Dada uma lista, crie outra só com os números positivos.
"""
numeros = [1, 2, 3, 4, 5, -5, -4, -3, - 2, -1]
numeros_positivos = []

for numero in numeros:
    if numero > 0:
        numeros_positivos.append(numero)

print(f'Lista: {numeros}')
print(f'Lista com números positivos: {numeros_positivos}')