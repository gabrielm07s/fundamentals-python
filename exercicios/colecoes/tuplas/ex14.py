"""
Desempacotamento básico: crie uma tupla com dados de um produto: ('Monitor Gamer', 1850.50, 15). 
Desempacote em variáveis nome, preco, estoque. Calcule e imprima o valor total em estoque formatado em R$.
"""
tupla = ('Monitor Gamer', 1850.50, 15)
nome, preco, estoque = tupla

valor_total = preco * estoque
print(f'Produto: {nome}')
print(f'Valor total: {valor_total:.2f}')