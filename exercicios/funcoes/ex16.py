"""
Crie criar_perfil(nome, **dados) que devolve um dicionário com nome e todos os dados extras 
(idade=19, cidade='Araxá'...). Mostre o resultado.
"""
def criar_perfil(nome, **dados):
    return { 'nome': nome, **dados }

dados = {'idade': 19, 'cidade': 'Araxá'}
print(criar_perfil('Gabriel', **dados))