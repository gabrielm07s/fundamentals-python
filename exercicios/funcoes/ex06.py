"""
Crie celsius_para_fahrenheit(c) e fahrenheit_para_celsius(f). 
Mostre uma tabela de 0 a 100 °C, de 20 em 20.
"""
def celsius_para_fahrenheit(c):
    f = (c * 1.8) + 32
    return f

def fahrenheit_para_celsius(f):
    c = ((f - 32) * 5) / 9
    return c

print('TABELA DE 0 A 100 ºC (DE 20 EM 20)')
for i in range(0, 101, 20):
    print(f'{i} ºC === {celsius_para_fahrenheit(i)} ºF')

print('\nTABELA DE 0 A 100 ºF (DE 20 EM 20)')
for i in range(0, 101, 20):
    print(f'{i} ºF === {fahrenheit_para_celsius(i):.1f} ºC')