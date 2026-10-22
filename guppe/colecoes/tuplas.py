"""
Tuplas

Tuplas são parecidas com listas, existem duas diferenças:

- Tuplas são representadas por parênteses()
- Tuplas são imutáveis, ao se criar um tupla ela não muda, toda operação em uma tupla
gera uma nova tupla

# Métodos para adicão e remoção de elementos nas tuplas não existem, dado que elas são imutáveis

Tuplas são mais rápidas do que listas
Tuplas deixam seu código mais seguro (Imutabilidade - traz segurança para o código)
"""
print(type(())) # tuple

# Tuplas são representadas por parênteses, mas podemos criá-las sem
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1, type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2, type(tupla2))

# Tupla com um elemento
tupla3 = (4) # isso não é uma tupla
print(tupla3, type(tupla3))

tupla4 = (4, ) # isso é uma tupla
print(tupla4, type(tupla4))

# Tuplas são definidas pela vírgula e não pelos parênteses
tupla5 = 4,
print(tupla5, type(tupla5))

# Gerando tupla com range
tupla = tuple(range(11))
print(tupla)

# Desempacotando tuplas
tupla = ('Gabriel', 'Miranda')
escola, sobrenome = tupla

print(escola, sobrenome)
# Gera erro se colocarmos um número diferente de elementos para desempacotar

# Podemos verificar a soma, valor máximo, valor mínimo e o tamanho
# OBS! todos os valores devem ser inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(f'\n{tupla}')
print(f'Soma: {sum(tupla)}')
print(f'Maior elemento: {max(tupla)}')
print(f'Menor elemento: {min(tupla)}')
print(f'Tamanho da tupla: {len(tupla)}')

# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2

print()
print(tupla1)
print(tupla2)
print(tupla3)

# Verificar se um elemento está contido na tupla
tupla = (1, 2, 3)
print(4 in tupla)

# Iterando sobre uma tupla
for n in tupla:
    print(n, end= ' ')

print()
for i, v in enumerate(tupla):
    print(f'[{i}], {v}')

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla.count('a'))

# Conseguimos transformar uma string em uma tupla
escola = tuple('Geek University')

print(escola)
print(escola.count('e'))

# Usar tuplas quando não precisar modifcar os dados contidos em uma coleção
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro'
         'Outubro', 'Novembro', 'Dezembro')

# meses.append('OLA') # erro

# O acesso de elementos de uma tupla é semelhante a uma lista
print(meses[5])

# Verificar qual índice um elemento está na tupla
print(meses.index('Junho'))

# Fatiamento
# tupla[inicio:fim:passo]
print(meses[0:])
print(meses[0:])
print(meses[5:9])

# Copiando uma tupla para outra
tupla = (1, 2, 3)
nova = tupla

print(tupla)
print(nova)

outra = (4, 5, 6)
nova += outra

print(nova)