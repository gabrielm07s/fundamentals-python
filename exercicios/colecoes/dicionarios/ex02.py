"""
Adicione a chave profissao, altere a idade e remova a cidade. Imprima após cada passo.
"""
nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
cidade = input('Digite a cidade: ')

pessoa = {
    'nome': nome, 
    'idade': idade, 
    'cidade': cidade
}
print(pessoa)

profissao = input('Digite a profissão: ')
pessoa.update({'profissao': profissao})
print(pessoa)

pessoa.update({'idade': 20})
print(pessoa)

pessoa.pop('cidade')
print(pessoa)