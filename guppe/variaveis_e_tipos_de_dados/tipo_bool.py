"""
Tipo Booleano

Temos dois valores: True (verdadeiro) ou False (falso)
OBS! Inicial sempre maiúscula

Usamos booleanos para realização de comparações e operações básicas
"""
ativo = True
print(ativo)

"""
Operações básicas:

Negação (not) - realizando a negação, se o valor booleano for verdadeiro, o resultado será falso,
se for falso o resultado será verdadeiro, ou seja, a operação not faz a inversão lógica
"""
print(not ativo)

"""
Ou (or) - é uma operação binária, depende de dois valores, ou um ou outro devem ser verdadeiros,
se ao menos um valor for verdadeiro irá retornar o valor verdadeiro
"""
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

logado = False
print(ativo or logado) # True

"""
E (and) - é uma operação binária, depende de dois valores, um e o outro devem ser verdadeiros,
se ao menos um valor for falso a condição será falsa
"""
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

"""
Podemos fazer operações de comparação também que retornam valores booleanos
"""
print(5 > 6)
print(5 < 6)
print(6 == 6)
print(4 <= 4)

"""
Podemos juntar expressões com os operadores lógicos
"""
num1 = 2
num2 = 3

print(num1 < num2 or num1 > 3)