"""
Verifique se uma lista está ordenada em ordem crescente
"""
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista)