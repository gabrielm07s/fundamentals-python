"""
Peça dois números e mostre soma, subtração, multiplicação, divisão, divisão inteira (//), resto (%) e potência (**).
"""
n1 = input('Digite o 1º número: ')
n2 = input('Digite o 2º número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
except:
    print('Digite um valor inteiro válido')
    raise

print()
print(f'Soma: {n1 + n2}')
print(f'Subtração: {n1 - n2}')
print(f'Multiplicação: {n1 * n2}')
print(f'Divisão: {n1 / n2}')
print(f'Divisão inteira: {n1 // n2}')
print(f'Módulo (Resto): {n1 % n2}')
print(f'Potência: {n1 ** n2}')
