"""
Dicionários (tipo dict)
Dicionários são estruturas de dados do tipo par "chave" e "valor"

Chaves podem ser consideradas como "índices" e podem ser de tipos imutáveis como:
    - str, int, float, bool, tuple, etc...
O valor pode ser de qualquer tipo, incluindo até mesmo outro dicionário

Usamos chaves {} para a clase dict para criarmos dicionários

Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
"""
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
print(pessoa, type(pessoa))
print(pessoa['nome'])

print()
for chave in pessoa:
    print(chave, pessoa[chave])