"""
Imprima todas as chaves, todos os valores e todos os pares
"""
nome = input('Nome: ')
idade = input('Idade: ')

dicionario = {
    'nome': nome, 
    'idade': idade
}

# print(dicionario.items())

print('\nChaves: ')
for d in dicionario.keys():
    print(d)

print('\nValores: ')
for d in dicionario.values():
    print(d)

print('\nPares de valores: ')
for d in dicionario.items():
    print(d)