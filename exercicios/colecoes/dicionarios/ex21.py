"""
Dado {'Ana': [8, 7], 'Bia': [5, 9]}, calcule a média de cada aluno e o aluno com maior média.
"""
alunos = {'Ana': [8, 7], 'Bia': [5, 9]}
aluno_media = {}

for chave, valor in alunos.items():
    nota1, nota2 = valor
    media_aluno = (nota1 + nota2) / 2.0

    aluno_media[chave] = media_aluno

print(aluno_media)
maior_media = max(aluno_media.values())

for chave, valor in aluno_media.items():
    if valor == maior_media:
        print(f'Maior média pertence a: {chave} - {valor:.2f}')