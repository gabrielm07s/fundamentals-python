"""
Reduce

OBS! A partir do Python 3+ a função reduce não é mais uma função integrada (built-in)
Para usarmos a função reduce, devemos importar a partir do módulo 'functools'

Utilizar a função reduce se realmente precisa dela, dependendo um laço for é mais legível

Temos uma coleção de dados:
dados = [a1, a2, a3, ...., an]

Temos uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

Assim como map e filter, a funcao reduce recebe dois parâmetros, uma função e um interável
reduce(funcao, dados)

A função reduce funciona:
-   res1 = f(a1, a2) # Aplica a função nos dois primeiro elementos da colecao e guarda o resultado
-   res2> res2 = f(res1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda por últomo

Em cada passo ela aplica a funcao passando como primeiro argumento o resultado de da aplicação anterior. No final,
reduce irá retornar final
"""
from functools import reduce

lista = [2, 3, 4,  5, 7, 11, 13, 19, 19]

# multiplicar todos os numeros de uma lista
multi = lambda x, y: x * y
res = reduce(multi, lista)
print(res)
