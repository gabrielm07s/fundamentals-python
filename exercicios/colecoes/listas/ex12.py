"""
Troque o maior e o menor elemento de lugar numa lista.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)

indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

lista[indice_maior], lista[indice_menor] = lista[indice_menor],  lista[indice_maior]
print(lista)