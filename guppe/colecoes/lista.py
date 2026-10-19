"""
Listas

Listas em Python funciona como vetores / matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado

- Dinâmico: não possui tamanho fixo (cria a lista e vai adicionando elementos), enquanto houver memória disponível pode adicionar elementos
- Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado

Listas em Python são representadas por colchetes: []
"""
print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27, 8]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(10))
lista5 = list('Geek University')

print(lista1)
print(lista2)
print(lista3)
print(lista4)

# Podemos checar se um determinado valor está contido na lista .__contains__()
num = 8
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

print(lista4.__contains__(num))

# Podemos ordenar uma lista .sort()
lista1.sort()
print(lista1)

# Podemos contar o número de ocorrências de um valor em uma lista .count()
print(lista1.count(1))
print(lista2.count('e'))

# Adicionar elementos em uma lista .append() - só conseguimos adicionar um elemento por vez
# Os valores sempre são adicionados no final da fila
print('\n', lista1)
lista1.append(42)
print(lista1)

# Podemos adicionar outros tipos de dados dentro de uma lista, até mesmo outra lista
# Porém adiciona os itens como formato de sublista
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67]) # adicionando itens também, porém aqui os itens são adicionados individualmente
print(lista1)
# extend() não aceita valores únicos, aceita apenas valores iteráveis, sempre atribui ao final da fila

# Podemos inserir um novo elemento na lista informando a posição do índice
# Não substitui o valor inicial, apenas será deslocado para a direita
lista1.insert(2, 'Novo valor')
lista1.insert(0, 'Olá mundo')
print(lista1)

# Podemos juntar duas listas
# Faz o mesmo que extend
lista6 = lista1 + lista2
print(lista6)

# Podemos inverter uma lista .reverse()
print()
print(lista1)
lista1.reverse()
print(lista1)

# Podemos inverter usando slice
print(lista1[::-1])

# Copiar uma lista
print()
lista7 = lista2.copy()
print(lista2)
print(lista7)

# Quantidade de elementos de uma lista len()
print()
print(len(lista2))

# Podemos remover o último elemento de uma lista, além de remover retorna o valor
print()
print(lista7)
lista7.pop()
print(lista7)

# Podemos remover um elemento pelo índice
# Os elementos a direita desse índice serão deslocados para a esquerda
print()
print(lista7)
lista7.pop(2)
print(lista7)

# Remover todos os elementos (zerar a lista)
print()
print(lista7)
lista7.clear()
print(lista7)

# É possível realizar a repetição de listas também
print()
nova_lista = [1, 2, 3]
print(nova_lista)
print(nova_lista * 3)

# Podemos converter uma string para uma lista
# split() de maneira padrão define o " " como forma de separar os elementos da lista
print()
curso = 'Programação Python Essencial'
print(curso)
curso = curso.split()
print(curso)

print()
curso = 'Programação,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
print()
lista8 = ['Programação', 'em', 'Python', 'Essencial']
print(lista8)

curso = ' '.join(lista8)
print(curso)

curso = '$'.join(lista8)
print(curso)

lista9 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45456446454]
print(lista9, type(lista9))
