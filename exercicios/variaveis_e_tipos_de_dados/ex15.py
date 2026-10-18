"""
Leia nome completo e mostre só o primeiro nome e só o último
"""
nome_completo = input('Nome completo: ').split()

# print(f'Seu nome completo é: {nome_completo}')
print(f'Primeiro nome: {nome_completo[0]}')
print(f'Último nome: {nome_completo[-1]}')