"""
Reproduza o bug de adicionar(valor, lista=[]) chamando-a 3 vezes e depois corrija usando None como padrão.
"""
def adicionar(valor, lista= None):
    lista.append(valor)
    return lista

lista_numeros = []
adicionar(4, lista_numeros)
adicionar(5, lista_numeros)
adicionar(6, lista_numeros)

print(lista_numeros)