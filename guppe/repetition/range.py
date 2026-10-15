"""
Ranges
São usados para gerar sequências numéricas, não de forma aleatória, mas de forma especificada

# 1. range(valor_de_parada) - valor não inclusivo, passo 1 e início padrão em 0
# 2. range(valor_de_inicio, valor_de_parada) - passo 1
# 3. range(valor_de_inicio, valor_de_parada, passo)
# 4. range(valor_de_inicio, valor_de_parada, passo) - para invertemos colocamos o passo negativo
"""
# 1.
print('Primeiro caso:')
for num in range(11):
    print(num, end= ' ')

# 2.
print('\n\nSegudo caso:')
for num in range(1, 11):
    print(num, end= ' ')

# 3.
print('\n\nTerceiro caso:')
for num in range(1, 11, 2):
    print(num, end= ' ')

# 4.
print('\n\nQuarto caso:')
for num in range(10, 0, -1):
    print(num, end= ' ')