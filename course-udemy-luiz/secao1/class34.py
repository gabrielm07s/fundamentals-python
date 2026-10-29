frase = 'Gabriel é Brabo'.lower()

i = 0
qtd_mais_vezes = 0
letra_maior = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_mais_vezes < qtd_letra_atual:
        qtd_mais_vezes = qtd_letra_atual 
        letra_maior = letra_atual

    i += 1

print(f'Letra que apareceu mais vezes: "{letra_maior}" - {qtd_mais_vezes}')