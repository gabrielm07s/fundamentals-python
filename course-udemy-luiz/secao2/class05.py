"""
Métodos úteis dos dicionários em Python

len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adicionar valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a achave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda'
}
# podemos usar get para retornar os valor de alguma chave
# se não existir, podemos passar um segundo parâmetro de valor padrão
print(p1.get('nome'))
print(p1.get('apelido', 'Não existe essa chave'))

# com pop conseguimos recuperar o valor que foi removido / deletado
# passamos a chave para remover o valor
nome_removido = p1.pop('nome')
print(nome_removido)

# retorna uma tupla com chave e valor e sempre remove o ultimo
sobrenome_removido = p1.popitem()
print(sobrenome_removido)

# atualizamos e podemos passar novos valores também
p1.update({
    'nome': 'Novo valor',
    'idade': 30,
})
print(p1)

# podemos passar de maneira nomeada
p1.update(apelido='Apelido')
print(p1)

# podemos usar tuplas também e listas
tupla = ('novo_valor', 'novo valor'), ('tupla', 2)
lista = [['nome', 'novo_valor'], ['idade', 30]]
p1.update(tupla)
print(p1)