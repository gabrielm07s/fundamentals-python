"""
Leia o nome de um estudante e diga em qual(is) curso(s) ele está: só Python, só Java, nos dois ou em nenhum.
"""
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

nome_estudante = input('Digite o nome de um estudante: ')

if nome_estudante in estudantes_python and nome_estudante in estudantes_java:
    print(f'O(a) estudante {nome_estudante} está presente nos dois cursos')
elif nome_estudante in estudantes_python and nome_estudante not in estudantes_java:
    print(f'O(a) estudante {nome_estudante} está presente no curso de Python')
elif nome_estudante not in estudantes_python and nome_estudante in estudantes_java:
    print(f'O(a) estudante {nome_estudante} está presente no curso de Java')
else:
    print(f'O(a) estudante {nome_estudante} não pertence a nenhum curso')