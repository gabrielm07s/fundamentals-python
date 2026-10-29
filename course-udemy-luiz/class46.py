"""
Tipo tupla = uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
print(nomes, type(nomes))

print(nomes[0], nomes[-1])

# podemos converter listas p/ tuplas
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
print(nomes, type(nomes))
