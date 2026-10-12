"""
PEP8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

The Zen of Python
import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilizar camelCase para nome de classes
[2] - Utilizar snake_case para funções ou variáveis
[3] - Utilizar 4 espaços para identação
[4] - Linhas em branco
    - Separar funções e definições de classes com duas linhas em branco
    - Métodos dentro de uma classe deve ser separados com uma única linha em branco
[5] - Imports
    - Imports devem ser sempre feitos em linhas separadas
    - Devem ser colocados no topo do arquivo, logo depois de quaisquer comentário
    ou docstring e antes de constantes ou variáveis globais
[6] - Espaços em expressões e instruções
[7] - Termine sempre uma instrução com uma nova linha

"""
# [5]
import os
import this
from types import (
    StringType,
    ListType
)

# [1]
class Calculadora:
    pass

class CalculadoraCientifica:
    pass

# [2]
def soma():
    pass

def soma_dois():
    pass

# [3]
numero = 4

numero_impar = 3

# [4]
if 'a' in 'banana':
    print('tem')

# [6]
funcao(algo[1], { outro: 2 })

algo(1)

dict['chave'] = list[indice]

x = 1
y = 2
long_variable = 3

# [7]
print('Algo')
