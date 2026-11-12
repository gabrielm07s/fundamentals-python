"""
List Comprehension em Python
List Comprehension é uma forma rápida para criar listas a partir 
de iteráveis
"""
print(list(range(10)))
print([x for x in range(10)])
print([x * 2 for x in range(10)])
print([x for x in range(10) if x % 2 == 0])