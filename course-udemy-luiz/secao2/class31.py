"""
raise - lançando exceções erros
"""
def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('_____')
        raise ZeroDivisionError('Divisão por zero não é permitido')

print(divide(8, 0))

def erro_divisao(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')

def divide(n, d):
    erro_divisao(d)
    return n / d

print(divide(8, 0))