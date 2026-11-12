"""
Reversed

Não confundir com a função reverse() em listas
A função reverse() funciona apenas em lista, enquanto a função reversed() funciona com qualquer iterável

Sua função é inverter o iterável
A função retorna um iterável chamado List Reverse Iterator
"""
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res, type(res))

# podemos converter o elemento retornado para uma lista, tupla ou conjunto
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))

# iterando sobre reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print()
# iterando sem for
print(''.join(list(reversed('Geek University')))) 

print('Geek University'[::-1])