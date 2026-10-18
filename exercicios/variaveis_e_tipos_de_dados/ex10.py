"""
Calcule o IMC (peso / altura²) e mostre com 1 casa decimal.
"""
peso = input('Digite o peso em kg: ')
altura = input('Digite a altura em m: ')

try:
    peso = float(peso)
    altura = float(altura)
except:
    print('Digite um valor válido')
    raise

imc = peso / (altura ** 2)

print(f'O valor do IMC é: {imc:.1f}')