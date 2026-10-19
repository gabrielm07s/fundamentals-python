"""
Calculadora simples: leia dois números e um operador (+ - * /), trate divisão por zero.
"""
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
operador = input('Digite um operador (+ - * /): ')

try:
    n1 = float(n1)
    n2 = float(n2)
except:
    print('Digite um valor válido')
    raise

resultado = 0
if operador == '+':
    resultado = n1 + n2
elif operador == '-':
    resultado = n1 - n2
elif operador == '*':
    resultado = n1 * n2
elif operador == '/':
    if n2 == 0:
        print('Divisão por zero é inválido')
        raise SystemExit
    resultado = n1 / n2
else:
    print('Operador não encontrado')
    raise SystemExit

print(f'{n1} {operador} {n2} = {resultado:.2f}')