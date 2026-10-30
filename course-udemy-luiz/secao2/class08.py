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
s1 = set()

# Adicionando itens
s1.add('Luiz')
s1.add(1)
print(s1)

# Atualizando dados (podemos passar vários valores desde que seja um iterável)
s1.update(('Olá mundo', 1, 2, 3, 4))
print(s1)

# Eliminar o valor que você quer
s1.discard('Olá mundo')
print(s1)

# Limpando dados
s1.clear()
print(s1)