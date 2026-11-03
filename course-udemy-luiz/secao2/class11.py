"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
"""
# Definição
def soma(x, y):
    print(f'{x=} {y=} | x + y = {x + y}')

# Executar uma função
soma(1, 4)
soma(4, 1)
# A ordem neste caso importa, pois são atribuídos de maneira sequencial

# Argumentos nomeados 
# Argumento é o valor que passamos para os parâmetros
soma(x=1, y=3)
soma(x=3, y=1)

def soma(x, y, z):
    print(f'{x=} {y=} {z=} | x + y + z = {x + y + z}')

# Ao passarmos um nomeado, todos os próximos devem ser nomeados
soma(2, 3, z=1)
soma(2, y=3, z=4)
