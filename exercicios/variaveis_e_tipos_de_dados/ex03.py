"""
Converta uma temperatura de Celsius para Fahrenheit (F = C * 9/5 + 32).
"""
temperatura_c = input('Digite a temperatura em Cº: ')

try:
    temperatura_c = float(temperatura_c)
except:
    print('Digite um valor de ponto flutuante válido')
    raise

temperatura_f = temperatura_c * (9 / 5) + 32

print(f'{temperatura_c:.1f} Cº equivale a {temperatura_f:.1f} Fº')