"""
Dados a = {1, 2} e b = {1, 2, 3, 4}, diga se a é subconjunto de b e se b é superconjunto de a.
"""
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
print(b.issuperset(a))

# issubset -> A é um SUBCONJUNTO de B
# issuperset -> B é um SUPERCONJUNTO (CONTÊM) A