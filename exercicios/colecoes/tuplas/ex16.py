"""
Descarte de valores com _: crie uma tupla com dados pessoais: ('Carlos', 32, 'Analista', 'Belo Horizonte', 6500.0). 
Desempacote extraindo apenas o nome e o salario, utilizando a convenção _ para ignorar os outros campos.
"""
dados_pessoais = ('Carlos', 32, 'Analista', 'Belo Horizonte', 6500.0)
nome, *_, salario = dados_pessoais

print(f'Nome: {nome}\nSalário: {salario:.2f}')