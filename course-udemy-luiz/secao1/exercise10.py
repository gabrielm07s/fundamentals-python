import os

palavra_secreta = 'teste'
letras_corretas = ''
tentativas = 0

while True:    
    letra_atual = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_atual) > 1:
        print('Digite apenas uma letra')
        continue


    if letra_atual in palavra_secreta:
        letras_corretas += letra_atual

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formata: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou!')
        print(f'A palavra final era: {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letras_corretas = ''
        tentativas = 0