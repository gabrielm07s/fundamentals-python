"""
Caixa eletrônico: leia o valor do saque e informe a menor quantidade de notas de 
100, 50, 20, 10, 5 e 2.
"""
valor_saque = input('Valor de saque: ')

try:
    valor_saque = int(valor_saque)
except:
    print('Digite um valor válido')
    raise

valor = valor_saque

notas100 = valor // 100
valor %= 100

notas50 = valor // 50
valor %= 50

notas20 = valor // 20
valor %= 20

notas10 = valor // 10
valor %= 10

notas5 = valor // 5
valor %= 5

notas2 = valor // 2
valor %= 2

print()
print(f'Valor de saque: {valor_saque}')
print(f'Notas de 100: {notas100}')
print(f'Notas de 50: {notas50}')
print(f'Notas de 20: {notas20}')
print(f'Notas de 10: {notas10}')
print(f'Notas de 5: {notas5}')
print(f'Notas de 2: {notas2}')
print(f'Moedas de 1: {valor}')