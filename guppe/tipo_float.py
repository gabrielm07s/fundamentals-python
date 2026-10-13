"""
Tipo numérico float

São os números com ponto flutuante, em Python a separação de casas decimais é feito com o ponto e não com vírgula
"""
print(1.443)
print(type(1.443))

# Podemos fazer dupla atribuição
valor1, valor2 = 1.40, 2.40
print('\n')
print(valor1, type(valor1))
print(valor2, type(valor2))

# Podemos converter float para int, nós perdemos a precisão nesta situação
res = int(valor1)
print('\n')
print(res, type(res))

# Podemos ter números complexos também
variavel = 5j
print('\n')
print(variavel, type(variavel))