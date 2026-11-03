"""
Crie somar_todos(*numeros) e media_de(*numeros). A média deve devolver 0 se nenhum número for passado.
"""
def somar_todos(*numeros):
    return sum(numeros)

def media_de(*numeros):
    if len(numeros) == 0:
        return 0
    
    media = sum(numeros) / len(numeros)
    return media

lista_numeros = [1, 2, 3, 4, 5, 6]
print(f'Lista de números: {lista_numeros}')
print(f'Soma de todos os números da lista: {somar_todos(*lista_numeros)}')
print(f'Média de todos os números da lista: {media_de(1, 2, 3, 4, 5)}')