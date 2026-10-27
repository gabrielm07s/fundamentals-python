"""
Lista de dicionários: cadastre 5 alunos (nome, nota1, nota2), calcule a média de cada um e mostre aprovados (>= 7).
"""
alunos = {}
for i in range(5):
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    alunos[nome] = [nota1, nota2]
    print()

print('Alunos Aprovados: ')
for chave, valor in alunos.items():
    nota1, nota2 = valor
    media_aluno = (nota1 + nota2) / 2.0

    if media_aluno >= 7.0:
        print(f'{chave} - {media_aluno:.2f}')

    
