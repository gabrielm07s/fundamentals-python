"""
Imprima a tabuada de um número lido (de 1 a 10).
"""
num = input('Digite um número (1 a 10): ')

try:
    num = int(num)
except:
    print('Digite um número válido')
    raise

if num < 1 or num > 10:
    raise SystemExit

for i in range(1, 11):
    print(f'{i} x {num} = {i * num}')
