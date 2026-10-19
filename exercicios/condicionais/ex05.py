"""
Leia a nota de um aluno e mostre Aprovado (>= 7), Recuperação (>= 5) ou Reprovado.
"""
nota = input('Digite a nota: ')

try:
    nota = float(nota)
except:
    print('Digite um valor válido')
    raise

print(f'\nNOTA = {nota:.2f}')

if nota >= 7:
    print('Aluno APROVADO')
elif nota >= 5:
    print('Aluno de RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')