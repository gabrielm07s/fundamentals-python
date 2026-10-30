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
"""
s1 = set() # set vazio
print(s1, type(s1))

s1 = set('Luiz')
print(s1) # set não garante a ordem

 