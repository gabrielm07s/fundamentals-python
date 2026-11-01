"""
Entendendo o *args

O *args é um parâmetro, ou seja, você pode chamar de qualquer coisa, desde que comece com asterisco
A convenção é *args

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla,
lembre-se que tuplas são imutáveis
"""
def soma(*args):
    return sum(args)

print(soma(1, 2, 3, 4, 5, 6))

# Desempacotamento
def soma(*args):
    return sum(args)

lista = [1, 2, 3, 4, 5, 6]
print(soma(*lista)) 

# Asterisco neste caso serve para informar que estamos passando como argumento
# uma coleção de dado, ele sabe que precisa desempacotar estes dados antes