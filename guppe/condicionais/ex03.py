num = input('Digite um número inteiro: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')
