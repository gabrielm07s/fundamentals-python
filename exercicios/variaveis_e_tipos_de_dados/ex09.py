"""
Leia um número decimal e mostre a parte inteira e a parte fracionária.
"""
num = input('Digite um número de ponto flutuante: ')

try:
    num = float(num)
except:
    print('Digite um número válido')
    raise

parte_inteira = int(num)
parte_fracionaria = num - parte_inteira


print(f'Número: {num}')
print(f'Parte inteira: {parte_inteira}')
print(f'Parte fracionária: {parte_fracionaria:.2f}')
