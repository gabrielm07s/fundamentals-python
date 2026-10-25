"""
Posições dos pares: leia 6 números inteiros em uma tupla. 
Percorra a tupla e mostre apenas os valores que forem pares e em quais índices eles se encontram.
"""
numeros = ()
for i in range(6):
    num = input(f'Digite o {i + 1}º número: ')

    try:
        num = int(num)
    except:
        print('Digite um número válido')
        raise

    tupla_num = (num, )
    numeros += tupla_num

print('\nNúmeros pares e seus índices: ')
for i, valor in enumerate(numeros):
    if valor % 2 == 0:
        print(f'índice: {i}, valor: {valor}')