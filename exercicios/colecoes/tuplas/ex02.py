"""
Tupla unitária: crie uma variável com x = (42) e outra com y = (42,). Mostre o valor e o type() de cada uma, 
exibindo uma mensagem que explique a função da vírgula.
"""
x = (42)
y = (42, )

print(f'Tipo da variável "x": {type(x)}')
print(f'Tipo da variável "y": {type(y)}')

# Isso acontece porque tuplas são definidas por vírgulas e não por parênteses e quanto tem apenas um elemento
# deve explicitamente usar vírgula para determinar uma tupla