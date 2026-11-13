"""
Try, except, else e finally
"""
a = 18
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print('Divisão por zero não é permitido')
except NameError:
    print('Nombe b não está definido')
except (TypeError, IndexError) as error:
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)