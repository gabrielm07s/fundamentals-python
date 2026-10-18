"""
Peça o nome e a idade e imprima: Olá, <nome>! Você tem <idade> anos. usando f-string.
"""
nome = input('Digite seu nome: ')
idade = input('Digite a idade: ')

try:
    idade = int(idade)
except:
    print('Digite um inteiro válido')
    raise

print(f'Olá {nome}! Você tem {idade} anos.')
