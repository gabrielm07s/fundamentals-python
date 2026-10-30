"""
Sets - Conjuntos em Python (tipo set)
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitas apenas tipos imutáveis como valor interno

# Criando um set
set(iterável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados de iteráveis
- não aceitam valores mutáveis
- não tem índices (index)
- eles não garantem ordem
- eles são iteráveis (for, in, not in)

Método úteis:
add, update, clear, discard

Operadores úteis
união -> (union |) (une ambos)
intersecção -> (intersection &) (itens presentes em ambos)
diferença -> itens presentes apenas no set da esquerda (difference -)
diferença simétrica -> itens que não estão em ambos (differente_symetric ^)
"""
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# union
s3 = s1.union(s2)
s3 = s1 | s2
print(s3)

# intersecção
s4 = s1.intersection(s2)
s4 = s1 & s2
print(s4)

# diferença (a ordem importa)
s5 = s1.difference(s2)
s5 = s1 - s2
print(f'Diferença entre s1 e s2: {s5}')

s6 = s2.difference(s1)
s6 = s2 - s1
print(f'Diferença entre s2 e s1: {s6}')

# diferença simétrica 
s7 = s1.symmetric_difference(s2)
s7 = s1 ^ s2
print(f'Diferença simétrica: {s7}')