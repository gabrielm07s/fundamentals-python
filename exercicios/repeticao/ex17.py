"""
Jogo de adivinhação: o programa sorteia (random.randint) de 1 a 100 e dá dicas "maior"/"menor" até acertar, contando as tentativas.
"""
import random
numero_sorteado = random.randint(1, 100)
# print(numero_sorteado)

tentativas = 0

while True:
    numero_digitado = input('Digite um número: ')
  
    try:
        numero_digitado = int(numero_digitado)
    except:
        print('Digite um número válido')
        raise
    
    tentativas += 1

    if numero_digitado > numero_sorteado:
        print(f'O número sorteado é MENOR que {numero_digitado}\n')
    elif numero_digitado < numero_sorteado:
        print(f'O número sorteado é MAIOR que {numero_digitado}\n')
    else:
        print('Parabéns você acertou!')
        break

print(f'Tentativas necessárias: {tentativas}')

