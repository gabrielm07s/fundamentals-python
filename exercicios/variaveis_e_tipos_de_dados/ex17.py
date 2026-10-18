"""
Leia o salário e o percentual de aumento e mostre o novo salário formatado como R$ 1.234,56.
"""
salario = input('Digite seu salário: ')
percentual = input('Digite o percentual de aumento (%): ')

try:
    salario = float(salario)
    percentual = float(percentual)
except:
    print('Digite um valor válido')
    raise

salario *= (1 + (percentual / 100))
salario_formatado = f'{salario:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

print(f'Salário: R$ {salario_formatado}')