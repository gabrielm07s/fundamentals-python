"""
Imprima um triângulo de asteriscos de altura n (for aninhado):
*
**
***
"""
altura_n = input('Digite uma altura n: ')

try:
    altura_n = int(altura_n)
except:
    print('Digite um número válido')
    raise

for i in range(1, altura_n + 1):
    for j in range(1, i + 1):
        print('*', end= '')
    print()