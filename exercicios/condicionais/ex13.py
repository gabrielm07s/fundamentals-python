"""
Leia o salário e calcule o imposto: até R$ 2.000 isento; de 2.000,01 a 3.000 → 8%; 
de 3.000,01 a 4.500 → 18%; acima → 28%.
"""
salario = input('Digite o salário: ')
imposto = 0

try:
    salario = float(salario)
except:
    print('Digite um valor válido')
    raise

if salario <= 2000:
    imposto = 0
elif salario <= 3000:
    imposto = 8
elif salario <= 4500:
    imposto = 18
else: 
    imposto = 28

salario_imposto = salario * (imposto / 100)

print(f'O valor imposto é de {salario_imposto:.2f}')
