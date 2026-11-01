"""
Funções com Retorno

OBS! Em Python quando uma função não retorna nenhum valor, o retorno é None
OBS! Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return
OBS! Não precisamos criar uma variável para receber o retorno de uma função, podemos passar a execução
da função para outras funções

OBS! Sobre a palavra return:
    - Ela finaliza a função, ou seja, ela sai da execução da função
    - Podemos ter em uma função, diferentes returns (sempre retorna apenas um deles)
    - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores
"""
numeros = [1, 2, 3]
numero_removido = numeros.pop() # neste caso a função tem retorno
print(f'Número removido: {numero_removido}')

ret_print = print('Python!')
print(ret_print) # print não tem retorno, no entanto que volta None

# Criando funções com retorno
def quadrado_7():
    return 7 ** 2

resultado = quadrado_7()
print(f'O resultado do quadrado de 7 é: {resultado}')

print(f'Executando diretamente sem função: {quadrado_7()}')

def diz_oi():
    return 'Oi '

print(diz_oi())

alguem = 'Pedro!'
print(diz_oi() + alguem)

def diz_oi():
    print('Estou sendo executado antes do retorno....')
    return 'Oi! '
    print('Estou sendo executado após o retorno....')

print(diz_oi())

def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

# função para jogar uma moeda
from random import random

def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())