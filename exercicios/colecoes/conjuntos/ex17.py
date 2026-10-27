"""
Mostre quantos estudantes existem no total e quantos estudam as duas linguagens.
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

total_estudantes = estudantes_python | estudantes_java
ambas_linguagens = estudantes_python & estudantes_java

print(f'Total de estudantes: {len(total_estudantes)}')
print(f'Total de estudantes das duas linguagens: {len(ambas_linguagens)}')