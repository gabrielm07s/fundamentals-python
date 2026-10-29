"""
Operação Ternária (Condicional de uma linha)
<valor> if <condicao> else <outro_valor>
"""
print('Valor' if True else 'Outro Valor')

variavel = 'Hello World' if 20 < 23 else 'Not'
print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)