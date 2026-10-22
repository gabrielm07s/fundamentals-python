"""
Some só os elementos nas posições pares da lista (0, 2, 4...).
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in range(len(numeros)):
    if i % 2 == 0:
        soma += numeros[i]

print(f'A soma dos elementos nas posições pares são: {soma}')