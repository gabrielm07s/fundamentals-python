"""
Mostre quem estuda as duas linguagens usando intersection() e depois &.
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

ambos_estudantes = estudantes_python.intersection(estudantes_java)
print(f'Ambos estudantes: {ambos_estudantes}')