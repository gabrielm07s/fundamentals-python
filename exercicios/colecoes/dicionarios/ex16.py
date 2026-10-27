"""
Estoque: dicionário produto → quantidade; leia uma venda e diminua o estoque, avisando se não há quantidade suficiente.
"""
estoque = {
    'Arroz': 4,
    'Feijão': 5,
    'Pão': 10
}

produto = input('Digite o produto comprado: ')
quantidade = int(input('Digite a quantidade comprada: '))

if produto in estoque:
    if quantidade <= estoque[produto] and quantidade > 0:
        estoque[produto] -= quantidade
        print(f'Compra realizada! Novo estoque de {produto}: {estoque[produto]}')
    else:
        print(f'Erro: estoque insuficiente. Temos apenas {estoque[produto]} unidades disponíveis')
else:
    print('Erro: produto não encontrado no estoque') 