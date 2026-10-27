"""
Dada uma lista com números repetidos, remova os duplicados convertendo para conjunto e volte para lista. Compare o tamanho antes e depois.
"""
numeros = [1, 2, 3, 3, 4, 5, 6, 6]
numeros_distintos = list(set(numeros))

print(f'Números originais: {numeros}')
print(f'Tamanho original: {len(numeros)}')
print(f'Números distintos: {numeros_distintos}')
print(f'Tamanho distintos: {len(numeros_distintos)}')