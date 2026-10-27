"""
Mostre todos os estudantes (sem repetir) usando union() e depois usando |.
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

todos_estudantes = estudantes_python.union(estudantes_java)
print(f'Todos os estudantes: {todos_estudantes}')