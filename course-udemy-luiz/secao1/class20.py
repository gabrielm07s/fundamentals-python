"""
Operadores Lógico (NOT)

NOT - usado para inversão lógica de expressões

not True = False
not False = True
"""
senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')

"""
TABELA-VERDADE:
|   C1   |  not C1 |
|  True  |  False  |
|  False |  True   |
"""

print('TABELA VERDADE:')
print('not True:', not True)
print('not False:', not False)
