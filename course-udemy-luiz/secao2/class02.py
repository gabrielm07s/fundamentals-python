# Manipulando chaves e valores em dicionários
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}

pessoa['apelido'] = 'Luiz' # criando uma chave
print(pessoa)
print(pessoa['apelido'])

# chaves dinâmicas
chave = 'nome'
pessoa[chave] = 'Luiz Otário' # atualizando a chave nome
print(pessoa)

del pessoa['sobrenome']
print(pessoa.get('sobrenome', 'Não existe'))