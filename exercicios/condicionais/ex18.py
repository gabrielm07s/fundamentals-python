"""
Leia o peso e a altura e classifique o IMC (abaixo do peso, normal, sobrepeso, obesidade).
"""
peso = input('Peso: ')
altura = input('Altura: ')

try:
    peso = float(peso)
    altura = float(altura)
except:
    print('Digite um valor válido')
    raise

imc = peso / (altura ** 2)

print()
print(f'IMC: {imc:.1f}')

if imc <= 18.5:
    print('Baixo peso / Magreza')
elif imc > 18.5 and imc < 25:
    print('Peso normal / Saudável')
elif imc >= 25 and imc < 30:
    print('Sobrepeso (pré-obesidade)')
elif imc >= 30 and imc < 35:
    print('Obesidade grau I')
elif imc >= 35 and imc < 40:
    print('Obesidade grau II (Severa)')
else: 
    print('Obesidade grau III (Mórbida ou Grave)')