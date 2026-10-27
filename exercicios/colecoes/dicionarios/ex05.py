"""
Peça uma chave e mostre o valor dela; se não existir, mostre Chave não encontrada
"""
nome = input('Nome: ')
idade = input('Idade: ')

dicionario = {
    'nome': nome, 
    'idade': idade
}

chave = input('Digite uma chave: ').lower()

"""
if chave in dicionario.keys():
    print(f'Encontrei a chave {chave}')
else:
    print(f'Não encontrei a chave {chave}')
"""

print(dicionario.get(chave, f'Não encontrado a chave: {chave}'))