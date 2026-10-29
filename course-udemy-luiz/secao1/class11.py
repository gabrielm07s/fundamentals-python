"""
Introdução a f-strings (formatação de strings)
"""
nome = 'Gabriel'
altura = 1.75
peso = 80
imc = peso / (altura ** 2)

print(f'{nome} tem {altura:.2f} de altura, pesa {peso} kg e seu imc é {imc:.2f}')