"""
Carrinho de compras: produto → {'preco': ..., 'qtd': ...}; mostre o total da compra com 2 casas decimais.
"""
carrinho = []

while True:
    print('[1] - Adicionar Produto')
    print('[2] - Listar Produtos')
    print('[3] - Sair')
    op = int(input('Digite sua opção: '))

    if op == 1:
        nome_produto = input('Nome do produto: ')
        preco_produto = float(input('Digite o preço do produto: '))
        qtd_produto = float(input('Digite a quantidade do produto: '))

        carrinho.append({'preco': preco_produto, 'quantidade': qtd_produto})
        print(f"Produto adicionado com sucesso: {{'{nome_produto}' - '{preco_produto}' - '{qtd_produto}'}}")
    elif op == 2:
        print(carrinho)
    elif op == 3:
        break
    else:
        print('Opção inválida')
    print()


total = 0
for produto in carrinho:
    total += produto['preco'] * produto['quantidade']

print(f'\nCarrinho: {carrinho}')
print(f'Total da compra: R$ {total:.2f}')