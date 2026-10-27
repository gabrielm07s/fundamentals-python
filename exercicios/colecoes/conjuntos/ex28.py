"""
Mostre os elementos que estão em apenas um dos dois conjuntos (diferença simétrica) e confira se o resultado é igual a (a - b) | (b - a).
"""
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {2, 4, 5, 7, 9, 10}

diferenca_ab = a - b
diferenca_ba = b - a

print(f'Diferença ab: {diferenca_ab}')
print(f'Diferença ba: {diferenca_ba}')

if diferenca_ab == diferenca_ba:
    print('Diferença simétrica')
else:
    print('Não é diferença simétrica')