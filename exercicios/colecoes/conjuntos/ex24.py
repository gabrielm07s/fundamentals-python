"""
Cadastro de e-mails: menu em while com adicionar, remover, buscar, listar e sair. 
Não permita e-mails repetidos e avise quando tentar adicionar um que já existe.
"""
conjunto_email = set()
while True:
    print('[1] Adicionar')
    print('[2] Remover')
    print('[3] Buscar')
    print('[4] Listar')
    print('[5] Sair')
    op = int(input('Digite sua opção: '))

    if op == 1:
        email = input('Digite o email que deseja adicionar: ')

        if email in conjunto_email:
            print('Não é permitido adicionar um email já cadastrado. Tente novamente!')
            break
        else:
            conjunto_email.add(email)

        print(f"Email adicionado com sucesso: '{{{email}}}'")
    elif op == 2:
        email = input('Digite o email que deseja remover: ')

        if email in conjunto_email:
            conjunto_email.remove(email)
            print(f"Email removido: '{{{email}}}'")
        else:
            print('O email não encontrado, tente novamente!')
            break
    elif op == 3:
        email = input('Digite o email que deseja buscar: ')

        if email in conjunto_email:
            print(f'Email encontrado: {email}')
        else:
            print('Email não encontrado, tente novamente!')
            break
    elif op == 4:
        print(f'Emails: {conjunto_email}')
    elif op == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida, tente novamente!')
    print()
