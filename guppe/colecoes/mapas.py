"""
Mapas - conhecidos em Python como Dicionários

Dicionários em Python são representados por cahves {}
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Iterando em todas as chaves
print(receita.keys())

# pdodemos iterar
for chave in receita.keys():
    print(receita[chave])

# Iterando em todos os valor:
print(receita.values())

for valor in receita.values():
    print(valor)

# desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma, Valor Máximo, Valor Mínimo, Tamanho
# Se todos os valores forem inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(sum(receita.values()))
print(len(receita))