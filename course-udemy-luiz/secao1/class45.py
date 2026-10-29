"""
Introdução ao desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes

print(nome1)
print(nome2)
print(nome3)

# usando o * podemos passar todo os outros valores
# para a variável
nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)
print(_)
# usamos "_" como forma de mostrar que não vai usar
