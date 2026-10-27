"""
Agrupe uma lista de dicionários de pessoas por cidade: {'SP': ['Ana', 'Bia'], 'RJ': ['Caio']}.
"""
pessoas = {}

while True:
    estado = input('Estado: ')
    nome = input('Nome: ')

    if estado in pessoas:
        pessoas[estado].append(nome)
    else:
        pessoas[estado] = [nome]

    op = input('Deseja sair? [S] / [N] ').upper()
    print()

    if op == 'S':
        break
   
print(pessoas)