"""
Mostre a lista invertida de três jeitos
"""
lista = [1, 2, 3, 4, 5, 6]

print(f'Reversa da forma 1: {lista[::-1]}')

lista.reverse()
print(f'Reversa da forma 2: {lista}')

lista = [1, 2, 3, 4, 5, 6]
print('Reversa da forma 3: ', end= ' ')

for i in range(len(lista) - 1, -1, -1):
    print(lista[i], end= ' ')