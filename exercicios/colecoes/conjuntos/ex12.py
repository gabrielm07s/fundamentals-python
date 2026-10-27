"""
Crie um conjunto s, faça novo = s e adicione um elemento em novo. Depois repita com novo = s.copy(). 
Imprima s nos dois casos para mostrar a diferença.
"""
# Shallow Copy
s = {1, 2, 3}
novo = s
novo.add(4)
print(f'Novo: {novo}')
print(f'Original: {s}')

# Deep Copy
s = {1, 2, 3}
novo = s.copy()
novo.add(4)
print(f'\nNovo: {novo}')
print(f'Original: {s}')