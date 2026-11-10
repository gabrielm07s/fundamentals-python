"""
Generators (Tuple Comprehensions)
"""
import sys 
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# Podemos fazer:
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res, type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(res, type(res))
# Performance melhor (ocupa menos recurso em memória)

# getsizeof -> retorna a quantidade de bytes em memória do elemento passado como parâmetro
# mostra quantos bytes a string 'Geek' está ocupando em memória, quanto maior a string, mais espaco ocupa
print(sys.getsizeof('Geek'))

# Gerando uma lista de números com List Comprehension
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
set_comp = sys.getsizeof({x * 10 for x in range(1000)})
dict_comp = sys.getsizeof({x: x * 10 for x in range(1000)})
gen = sys.getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator: {gen} bytes')

# Iterando sobre Generator Expression
gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)