"""
Leia um número e diga se é par ou ímpar.
"""
num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

if num % 2 == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')
