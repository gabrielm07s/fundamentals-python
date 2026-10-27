"""
Demonstre a diferença entre b = a e b = a.copy() alterando b e imprimindo a.
"""
a = {1: 2, 3: 4}
b = a
b.update({5: 6})
print(a)
print(b)

b = a.copy()
b.update({7: 8})
print(a)
print(b)