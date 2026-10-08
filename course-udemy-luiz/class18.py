"""
Operadores Lógicos (AND)

AND - todas as condições (expressões) precisam ser verdadeiras,
se tiver qualquer valor considerado falso, a expressão inteira
será falsa

Valores FALSY (em contexto booleano são False):
    0, 0.0, '', "", False

None - tipo que é usado para representar um NÃO valor
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar\n')
else:
    print('Sair\n')

"""
TABELA-VERDADE:
|   C1   |  C2   |  C1 and C2 |
|  True  | True  |    True    |
|  True  | False |    False   |
|  False | True  |    False   |
|  False | False |    False   |
"""

print('TABELA VERDADE:')
print('True AND True:', True and True)
print('True AND False:', True and False)
print('False AND True:', False and True)
print('False AND False:', False and False)