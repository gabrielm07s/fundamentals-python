"""
Peça o raio de um círculo e calcule a área (π * r²) com 2 casas decimais (:.2f).
"""
from math import pi

raio = input('Digite o raio do círculo: ')

try:
    raio = float(raio)
except:
    print('Digite um valor válido')
    raise

area = pi * (raio ** 2)

# print(f'PI: {pi:.2f}') # 3.14
print(f'Área do círculo: {area:.2f}')