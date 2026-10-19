"""
Leia um número e diga se é positivo, negativo ou zero.
"""
num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

if num > 0:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'O número {num} é negativo')
else:
    print(f'O número {num} é nulo')