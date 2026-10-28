"""
Módulo Collections - Ordered Dict
Em dicionários, a ordem de inserção dos elementos não é garantida
Usando Ordered Dict garantimos essa ordem completa da inserção dos elementos, 
temos uma performance melhor

# dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# for chave, valor in dicionario.items():
#     print(f'chave={chave}: valor={valor}')
"""
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

# Diferença entre dict e Ordered Dict
# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True, a ordem dos elementos não importa para os dicionários

# Ordered Dict
dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})
print(dict1 == dict2) # False, a ordem importa