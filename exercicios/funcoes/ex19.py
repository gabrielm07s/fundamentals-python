"""
Crie aplicar(funcao, lista) que devolve uma nova lista com funcao aplicada a cada item.
Use com len, str.upper e uma função sua.
"""
def aplicar(funcao, lista):
    resultado = []

    for item in lista:
        resultado.append(funcao(item))

    return resultado

def triplo(n):
    return n * 3

print(aplicar(len, ['a', 'bb']))
print(aplicar(str.upper, ['sol']))
print(aplicar(triplo, [1, 2]))