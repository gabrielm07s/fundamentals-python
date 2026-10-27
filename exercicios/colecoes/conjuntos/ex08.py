"""
Remova um elemento com remove() e depois tente remover um que não existe dentro de um try/except KeyError, 
com uma mensagem amigável.
"""
conjunto = {3, 6, 9, 12}
print(conjunto)

conjunto.remove(3)
print(conjunto)

try:
    conjunto.remove(10)
except KeyError:
    print('Não é possível remover o número pois ele não está presente no conjunto')