"""
Tabela de preços tabular: crie uma tupla de tuplas com produtos e preços:
"""
produtos = (
    ('Lápis', 1.75),
    ('Borracha', 2.00),
    ('Caderno Universitário', 19.90),
    ('Estojo', 12.50),
    ('Mochila Escolar', 149.90),
)

for nome, preco in produtos:
    print(f'{nome} - R$ {preco:>7.2f}')