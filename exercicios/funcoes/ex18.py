"""
Crie remover_duplicados(lista) que devolve uma lista nova sem repetidos (mantendo a ordem) 
sem alterar a lista original. Prove com assert.
"""
def remover_duplicados(lista):
    ja_visto = []

    for l in lista:
        if l in ja_visto:
            lista.pop(l)
        else:
            ja_visto.append(l)

    return lista

lista = [1, 1, 2, 3, 4, 5, 5, 6]
print(remover_duplicados(lista))