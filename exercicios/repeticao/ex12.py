"""
Peça uma senha até o usuário acertar (limite de 3 tentativas, use break).
"""
senha = '123456'
tentativas = 0

while True:
    senha_digitada = input('Digite a senha: ')
    tentativas += 1

    if senha_digitada == senha:
        print('\nVocê acertou a senha!')
        break
    else:
        print('Tente novamente....')
        print(f'Tentativas: {tentativas}\n')

    if tentativas == 3:
            print('Tentativas excedidas.')
            break