"""
Descubra se um número é primo.
"""
num = input('Digite um número: ')

try:
    num = int(num)
except:
    print('Digite um valor válido')
    raise

qtd_divisores = 0

for i in range(1, num + 1):
    if num % i == 0:
        qtd_divisores += 1

# print(f'Quantidade de divisores do número {num}: {qtd_divisores}')

if qtd_divisores == 2:
    print(f'O número {num} é PRIMO')
else:
    print(f'O número {num} NÃO É PRIMO')