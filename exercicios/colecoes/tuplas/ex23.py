"""
Boletim escolar com tuplas aninhadas: crie uma tupla com os registros de 4 alunos no formato 
(nome, (nota1, nota2, nota3)). Calcule e imprima a média de cada aluno e sua 
situação (Aprovado para média >= 7.0, Recuperação para média entre 5.0 e 6.9, Reprovado abaixo de 5.0).
"""
tupla_total = ()

for i in range(4):
    nome = input(f'Digite o nome do {i + 1}º aluno: ')
    nota1 = input(f'Digite a 1º nota do {i + 1} aluno: ')
    nota2 = input(f'Digite a 2º nota do {i + 1} aluno: ')
    nota3 = input(f'Digite a 3º nota do {i + 1} aluno: ')

    try:
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
    except:
        print('Digite um valor válido')
        raise

    tupla_aluno = (nome, (nota1, nota2, nota3))
    tupla_total += (tupla_aluno, )
    print()

for nome, (n1, n2, n3) in tupla_total:
    media = (n1 + n2 + n3) / 3.0

    print(f'Aluno: {nome}, Média: {media:.2f}', end= ' ') 
    if media >= 7.0:
        print('Situação: APROVADO')
    elif media >= 5.0:
        print('Situação: RECUPERAÇÃO')
    elif media < 5:
        print('Situação: REPROVADO')
    else:
        print('Nota inválida')
