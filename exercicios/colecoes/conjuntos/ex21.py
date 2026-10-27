"""
Dado um conjunto de inteiros, mostre sum, max, min e len, e calcule a média.
"""
numeros = {1, 2, 3, 4, 5, 6, 7, 10}

print(f'Conjunto: {numeros}')
print(f'Soma: {sum(numeros)}')
print(f'Valor máximo: {max(numeros)}')
print(f'Valor mínimo: {min(numeros)}')
print(f'Tamanho: {len(numeros)}')

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print(f'Média = {media:.2f}')
else:
    print('Não existe divisão por zero')