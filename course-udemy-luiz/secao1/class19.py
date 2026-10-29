"""
Operadores Lógicos (OR)

OR - qualquer condição verdadeira avalida toda a expressão
como verdadeira, ou seja, qualquer valor verdadeira considera
a expressão interia avaliada naquele valor

Valores FALSY (em contexto booleano são False):
    0, 0.0, '', "", False
Valores TRUTHY são todos com exceção destes

None - tipo que é usado para representar um NÃO valor
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if ((entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida):
    print('Entrar\n')
else:
    print('Sair\n')

"""
TABELA-VERDADE:
|   C1   |  C2   |  C1 or C2 |
|  True  | True  |    True    |
|  True  | False |    True    |
|  False | True  |    True    |
|  False | False |    False   |
"""

print('TABELA VERDADE:')
print('True OR True:', True or True)
print('True OR False:', True or False)
print('False OR True:', False or True)
print('False OR False:', False or False)