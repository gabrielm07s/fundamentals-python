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
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}

print(len(pessoa))
print()

print(list(pessoa.keys()))
print(f'Chaves:')
for chave in pessoa.keys():
    print(chave)
print()

print(list(pessoa.values()))
print(f'Valores:')
for valor in pessoa.values():
    print(valor)
print()

print(list(pessoa.items()))
print(f'Chave e Valor:')
for chave, valor in pessoa.items():
    print(chave, valor)
print()

pessoa.setdefault('idade', None)
print(pessoa['idade'])