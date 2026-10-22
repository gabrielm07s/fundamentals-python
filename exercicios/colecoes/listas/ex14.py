"""
Remova os valores duplicados de uma lista mantendo a ordem original
"""
lista = [1, 1, 1, 2, 3, 4, 4, 5]
lista_sem_duplicatas = []

for i in lista:
    if i not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(i)

print(lista_sem_duplicatas)