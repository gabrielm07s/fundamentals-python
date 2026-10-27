"""
Agenda de contatos: menu em while com adicionar, buscar, remover, listar e sair (nome → telefone).
"""
contatos = {}
while True:
    print('[1] - Adicionar')
    print('[2] - Buscar')
    print('[3] - Remover')
    print('[4] - Listar')
    print('[5] - Sair')
    op = int(input('Digite a sua opção: '))

    if op == 1:
        nome = input('Digite seu nome: ')
        telefone = input('Digite seu telefone: ')

        contatos[nome] = telefone
        print(f"Contato adicionado com sucesso: {{'{nome}': '{telefone}'}}")
    elif op == 2:
        contato = None
        nome = input('Deseja buscar qual contato? ')

        if nome in contatos:
            for chave, valor in contatos.items():
                if chave == nome: 
                    contato = {chave: valor}
    elif op == 3:
        nome = input('Qual nome você deseja remover? ')

        removido = contatos.pop(nome, None)

        if removido:
            print(f'O contato {nome} com o número {removido} foi excluído')
        else:
            print('Contato não encontrado')
    elif op == 4:
        print(f'Contatos: {contatos}')
    elif op == 5:
        break
    else:
        print('Operação inválida')
    print()