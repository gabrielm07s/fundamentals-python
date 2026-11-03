"""
Reproduza o bug de adicionar(valor, lista=[]) chamando-a 3 vezes e depois corrija usando None como padrão.
"""
def adicionar(valor, lista= []):
    lista.append(valor)
    return lista

print(adicionar(4))
print(adicionar(5))
print(adicionar(6))

# CORREÇÃO
print('\nCORREÇÃO:')
def adicionar(valor, lista= None):
    if lista is None:
        lista = []
    lista.append(valor)
    return lista

print(adicionar(4))
print(adicionar(5))
print(adicionar(6))