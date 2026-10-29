nome = input('Nome usuário: ')

tam_nome = len(nome)

if tam_nome <= 4:
    print('Seu nome é curto')
elif tam_nome >= 5 and tam_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')