"""
Crie area_retangulo(base, altura) e area_circulo(raio) (use math.pi). 
Leia os dados e mostre as duas áreas com 2 casas decimais.
"""
import math

def area_retangulo(base, altura):
    return base * altura

def area_circulo(raio):
    return math.pi * raio ** 2 

base = int(input('Digite o valor da base: '))
altura = int(input('Digite o valor da altura: '))
raio = int(input('Digite o valor do raio: '))

print('\nResultados: ')
print(f'Área retângulo: {area_retangulo(base, altura):.2f}')
print(f'Área círculo: {area_circulo(raio):.2f}')