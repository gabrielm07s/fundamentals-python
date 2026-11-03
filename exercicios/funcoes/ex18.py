"""
Crie remover_duplicados(lista) que devolve uma lista nova sem repetidos (mantendo a ordem) 
sem alterar a lista original. Prove com assert.
"""
def remover_duplicados(lista):
    ja_visto = []

    for elemento in lista:
        if elemento not in ja_visto:
            ja_visto.append(elemento)
    
    return ja_visto

lista = [1, 1, 2, 3, 4, 5, 5, 6]
print(f'Lista original: {lista}')
print(f'Lista sem repetidos: {remover_duplicados(lista)}')