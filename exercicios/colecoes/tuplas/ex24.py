"""
Estatísticas de funcionários: crie uma tupla com dados de funcionários 
((nome, setor, salario), ...). 
Calcule a média salarial da empresa e gere uma nova tupla apenas com os 
funcionários que recebem salário acima da média.
"""
dados_funcionarios = ()

n = input('Digite a quantidade de funcionários: ')

try:
    n = int(n)
except:
    print('Digite um número válido')
    raise

for i in range(n):
    nome = input(f'Digite o nome do {i + 1}º funcionário: ')
    setor = input(f'Digite o setor do {i + 1}º funcionário: ')
    salario = input(f'Digite o salário do {i + 1}º funcionário: ')

    try:
        salario = float(salario)
    except:
        print('Digite um valor válido')
        raise SystemExit

    tupla_funcionarios = (nome, setor, salario)
    dados_funcionarios += (tupla_funcionarios, )
    print()

total_salario = 0

for funcionario in dados_funcionarios:
    total_salario += funcionario[2] 

if len(dados_funcionarios) > 0:
    media_salarial = total_salario / len(dados_funcionarios)
    print(f'Média salarial: {media_salarial}')
else:
    print('Não existe divisão por zero')
    raise SystemExit

for funcionario in dados_funcionarios:
    if funcionario[2] > media_salarial:
        print(f'Funcionário: {funcionario[0]}, Setor: {funcionario[1]}, Salário: {funcionario[2]}')