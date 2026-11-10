"""
Any e All

all() -> retorna True se todos os elementos do iterável são verdadeiros ou vazio
any() -> retorna True se qualquer elemento do iterável for verdadeiro, se o iterável estiver vazio é False
"""
print(all([0, 1, 2, 3, 4]))
print(all([]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all([nome[0] == 'C' for nome in nomes]))

# Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

print(any([0, 1, 2, 3, 4]))
print(any([]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
