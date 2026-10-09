"""
Calculadora

Entrada: n1, n2, operação
Operações: +, -, *, /
"""
while True:
    num1_str = input('\nDigite o primeiro número: ')
    num2_str = input('Digite o segundo número: ')
    operacao = input('Digite a operação: ')

    numeros_validos = None
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(num1_str)
        num2_float = float(num2_str) 
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-*/'

    if operacao not in operadores_permitidos:
        print('Operador inválido')
        continue

    resultado = 0

    if operacao == '+':
        resultado = num1_float + num2_float
    elif operacao == '-':
        resultado = num1_float - num2_float
    elif operacao == '*':
        resultado = num1_float * num2_float
    elif operacao == '/':
        if num2_float == 0:
            print('Divisão por zero não é possível')
        else:
            resultado = num1_float / num2_float
    else:
        print('Operação inválida')

    print(f'Resultado da operação: {resultado}')

    opcao = input('Deseja [s]air? ')
    
    if opcao.lower().startswith('s'):
        break