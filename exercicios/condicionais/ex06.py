"""
Leia três números e mostre o maior deles.
"""
n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')
n3 = input('Digite o 3º número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
except:
    print('Digite um número válido')
    raise

maior = max(n1, n2, n3)

print(f'O maior número é {maior}')