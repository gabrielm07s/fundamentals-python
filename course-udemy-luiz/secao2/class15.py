"""
arg - argumentos não nomeados
* - *args (empacotamento e desempactoamento)
"""
# lembre-se do desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6, 7))

