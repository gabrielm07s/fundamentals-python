num = input('Digite um número inteiro: ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

if num > 0:
    print(f'A raiz quadrada do número {num} é igual a {num ** (1/2):.2f}')
elif num < 0:
    print('O número é inválido')
else:
    print('Nada feito...')