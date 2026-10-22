"""
Junte duas listas ordenadas numa terceira também ordenada
"""
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [9, 8, 6, 34, 23, 13, 2, 1, 4, 5, 767]

# ordenando lista1
for i in range(len(lista1)):
    for j in range(i + 1, len(lista1)):
        if lista1[i] > lista1[j]:
            aux = lista1[i]
            lista1[i] = lista1[j]
            lista1[j] = aux

# ordenando lista2
for i in range(len(lista2)):
    for j in range(i + 1, len(lista2)):
        if lista2[i] > lista2[j]:
            aux = lista2[i]
            lista2[i] = lista2[j]
            lista2[j] = aux


# juntando em uma terceira lista
lista3 = lista1 + lista2

# ordenando lista3
for i in range(len(lista3)):
    for j in range(i + 1, len(lista3)):
        if lista3[i] > lista3[j]:
            aux = lista3[i]
            lista3[i] = lista3[j]
            lista3[j] = aux

print(lista1)
print(lista2)
print(lista3)