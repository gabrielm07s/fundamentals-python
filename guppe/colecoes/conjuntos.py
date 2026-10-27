"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos Conjuntos
da matemática

Conjuntos em Python são chamados de Sets
    - Não possuem valores duplicados
    - Não possuem valores ordenados
    - Elementos não são acessados via índice, ou seja, não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos
com a ordenação deles, quando não precisamos nos preocupar com chaves, valores e itens duplicados

Conjuntos são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários)
    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor
"""
# Definindo um conjunto
# Forma # 01
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s, type(s))
# Ao criar um conjunto caso seja adicionado um valor ja existente, o mesmo será ignorado
# sem gerar erros e não fará parte do conjunto

# Forma # 02 (mais comum)
s = {1, 2, 3, 4, 5, 5}
print(s, type(s))

# Podemos gerar conjuntos a partir de lista, tupla, string....
nome = 'Gabriel de Souza Miranda'
print(set(nome))

lista = [1, 2, 3, 4, 5, 5, 6]
print(set(lista))

tupla = (1, 2, 3, 4, 4, 5)
print(set(tupla))

# Verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# OBS! Não temos valores duplicados e não temos ordem

# Listas aceitam valores duplicados então temos 9 elementos
lista = [99, 2, 2, 34, 22, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados então temos 9 elementos
tupla = (99, 2, 2, 34, 22, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas então temos 7 elementos
dicionario = {}.fromkeys([99, 2, 2, 34, 22, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# COnjuntos não aceitam valores duplicados, então temos 7 elementos
conjunto = {99, 2, 2, 34, 22, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo conjunto, podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}
print(s, type(s))

# Podemos iterar sobre Sets
for valor in s:
    print(valor)

# Usos interessantes com Sets
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(len(cidades))
print(f'Cidades distintas: {set(cidades)}')

# Adicionando elementos ao conjunto
s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro, apenas é ignorado e não é adicionado
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma # 01
s.remove(3) # não é índice, informamos o valor a ser removido (pois conjuntos não são indexados)
print(s)
# OBS! Caso o valor não seja encontrado será gerado o erro KeyError

# Forma # 02
s.discard(2)
print(s)
# OBS! Caso o valor não for encontrado não gerará erro, será ignorado

# Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

# Forma # 01 (Deep Copy)
novo = s.copy()
novo.add(4)
print(novo)
print(s)

# Forma # 02 (Shallow Copy)
s = {1, 2, 3}
novo = s
novo.add(4)
print(novo)
print(s)

# Removendo todos os itens de um conjunto (limpeza do conjuto)
s.clear()
print(s)

# Métodos Matemáticos de Conjuntos
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Alguns alunos que estudam Python também estudam Java
# UNIÃO
# unioun (removendo duplicidades)
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1) # junta os dois conjuntos

# | (pipe) -> união (removendo duplicidades)
unicos2 = estudantes_python | estudantes_java
print(unicos2) 

# INTERSECÇÃO
# intersection (valor presentes nos dois conjuntos)
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# & -> intersecção (valor presentes nos dois conjuntos)
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que estão em um curso que não estão no outro
# difference (diferença)
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# - (diferença)
so_python = estudantes_python - estudantes_java
print(so_python)

so_java = estudantes_java - estudantes_python
print(so_java)

# Soma, Maior Valor, Valor Mínimo, Tamanho
# Se os valores forem todos inteiros ou reais
s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))