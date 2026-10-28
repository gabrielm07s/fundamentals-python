"""
Módulo Colections - Named Tuple
Named Tuple >> podemos nomear os elementos da tupla, são tuplas diferenciadas
onde podemos especificar um nome para a mesma e também parâmetros

# recap tupla:
tupla = (1, 2, 3)
print(tupla[1])
"""
from collections import namedtuple

# Precisamos definir o nome e parâmetros
# Forma 01 - Declaração
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 02 - Declaração
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 03 - Declaração
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade= 2, raca='Chow Chow', nome='Ray')
print(ray)

# Acessando os dados
# Forma 01
print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome

# Forma 02
print(ray.idade)
print(ray.raca)
print(ray.nome)

# tudo de tuplas pode ser usado aqui
print(ray.index('Chow Chow'))
print(ray.count('Chow Chow'))