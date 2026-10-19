"""
Leia a idade e diga se é maior de idade (>= 18).
"""
idade = input('Digite a idade: ')

try:
    idade = int(idade)
except:
    print('Digite um número válido')
    raise

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')