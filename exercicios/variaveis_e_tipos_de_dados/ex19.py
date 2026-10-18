"""
Leia o preço de um produto e mostre o valor à vista (10% de desconto) e em 3x sem juros.
"""
preco_produto = input('Preço do produto: ')

try:
    preco_produto = float(preco_produto)
except:
    print('Digite um valor válido')
    raise

desconto = 10

preco_produto_a_vista = preco_produto * (1 - (desconto / 100))
preco_produto_3x = preco_produto / 3

print(f'Valor à vista: {preco_produto_a_vista:.2f}')
print(f'Valor em 3x sem juros: {preco_produto_3x:.2f}')