"""
Valide uma senha: aceita se tiver 8+ caracteres e não for igual ao nome do usuário.
"""
nome_usuario = input('Digite o nome do usuário: ')
senha = input('Digite uma senha: ')

senha_valida = (len(senha) >= 8) and (senha != nome_usuario)

if senha_valida:
    print('Senha válida')
else:
    print('Senha inválida')