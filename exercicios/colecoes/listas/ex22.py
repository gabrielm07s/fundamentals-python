"""
Demonstre a diferença entre b = a e b = a.copy() alterando b e imprimindo a.
"""
a = [1, 2, 3, 4, 5]
b = a

b.append(6)

print(a)
print(b)

print()
a = [1, 2, 3, 4, 5]
b = a.copy()

b.append(6)

print(a)
print(b)