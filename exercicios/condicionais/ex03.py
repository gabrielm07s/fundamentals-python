"""
Leia dois números e diga qual é o maior (ou se são iguais).
"""
n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
except:
    print('Digite um número válido')
    raise

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n1} é menor que {n2}')
else:
    print(f'{n1} é igual a {n2}')