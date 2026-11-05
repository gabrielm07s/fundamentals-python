"""
Map

Com map fazemos mapeamento de valores para função
"""
import math

def area(r):
    """Calcula a área de um círcvulo com raio 'r'"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# forma map
# map recebe dois parâmetros, onde o primeiro é a função e o seguindo é um iterável
areas = map(area, raios)
print(areas, type(areas)) # Retorna um map object
print(list(areas)) # pode ser convertido para tupla também

# forma com map e lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS! Após utilizar a função map, depois da primeira utilização do resultado, ele zera
"""
Em Map temos dados iteráveis:
dados: a1, a2, ....., an
Temos uma função:
f(x)

Utilizamos a função map(f, dados) para "mapear" cada elemento dos dados e aplicar a função
"""
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27), ('Nova York', 28), ('Londres', 22)]

c_para_f = lambda dado: (dado[0], (dado[1] * 9/5) + 32)
print(list(map(c_para_f, cidades)))


