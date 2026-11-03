"""
Crie aplicar(funcao, lista) que devolve uma nova lista com funcao aplicada a cada item.
Use com len, str.upper e uma função sua.
"""
def aplicar(funcao, lista):
    return funcao(lista)

def triplo(lista):
    for i, valor in enumerate(lista):
        lista[i] = valor * 3
    return lista

lista = [1, 2, 3, 4, 5, 6]
print(aplicar(len, lista))
print(aplicar(str, lista))
print(aplicar(triplo, lista))