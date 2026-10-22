"""
Mostre o segundo maior valor de uma lista
"""
lista = [1, 2, 3, 4]

maior = lista[0]
segundo_maior = lista[0]

for numero in lista:
    if numero > maior:
        segundo_maior = maior
        maior = numero

    if numero > segundo_maior and numero != maior:
        segundo_maior = numero

print(f'Segundo maior: {segundo_maior}')