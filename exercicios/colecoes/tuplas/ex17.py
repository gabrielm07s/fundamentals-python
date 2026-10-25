"""
Swap com tuplas: leia dois valores a e b. 
Realize a troca dos valores em uma única linha (a, b = b, a) e imprima o resultado, 
explicando o que significa o empacotamento e desempacotamento nesse processo.
"""
a = 5
b = 8
print(f'{a=}, {b=}')

a, b = b, a
print(f'{a=}, {b=}')
