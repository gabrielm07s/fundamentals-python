"""
Crie um dicionário com nome, idade e cidade de uma pessoa e imprima cada valor.
"""
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
cidade = input('Digite a cidade: ')

pessoa = {
    'nome': nome, 
    'idade': idade, 
    'cidade': cidade
}

for p in pessoa.values():
    print(p)