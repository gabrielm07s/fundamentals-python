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
s1 = set() # set vazio
print(s1, type(s1))

s1 = set('Luiz')
print(s1) # set não garante a ordem

# sets não aceitam valores duplicados
s1 = {1, 2, 3, 4, 4, 4, 4, 1}
print(s1)

l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
# ao converter a lista remove elementos repetidos 
print(set(l1))

print(3 in s1)
print(4 in s1)

for numero in s1:
    print(numero)