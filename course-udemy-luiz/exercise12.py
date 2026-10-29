"""
Lista de Compras
Inserir, Apagar, Listar
Não permitir quebrar com erros de índices inexistentes
"""
import os
import time

carrinho = []
while True:
    print('---- LISTA DE COMPRAS ----')
    print('[1]. Adicionar')
    print('[2]. Remover')
    print('[3]. Listar')
    print('[4]. Sair')
    op = input('Digite uma opção: ')

    try:
        op = int(op)
    except:
        print('Digite um número válido.')

    if op == 1:
        nome_produto = input('Digite o nome do produto: ')
        preco_produto = float(input('Digite o preço do produto: '))
        qtd_produto = int(input('Digite a quantidade do produto: '))

        produto = (nome_produto, preco_produto, qtd_produto)
        carrinho.append(produto)
        print(f'Produto adicionado com sucesso!')
    elif op == 2:
        nome_produto = input('Digite o nome do produto que deseja remover: ')

        for nome, *_ in carrinho:
            if nome_produto == nome:
                produto_removido = carrinho.pop()
                print('Produto removido com sucesso!')
                break

        if not produto_removido:
            print('Produto não encontrado.')
    elif op == 3:
        print(f'Lista de Compras: {carrinho}')
    elif op == 4:
        print('Saindo...')
        time.sleep(3)
        os.system('cls')
        break
    else:
        print('Opção inválida!')
    
    time.sleep(3)
    os.system('cls')

print(f'\n=== LISTA COMPLETA:')

preco_total = 0
for produto in carrinho:
    nome, preco, quantidade = produto
    print(f'{nome.title()}: R$ {preco:.2f} - {quantidade}x')

    preco_total += (preco * quantidade)

print(f'\n=== PREÇO TOTAL: R$ {preco_total:.2f}')