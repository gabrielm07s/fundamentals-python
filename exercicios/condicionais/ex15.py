"""
Pedra, papel e tesoura entre duas pessoas (cada uma digita sua jogada).
"""
jogada1 = input('PEDRA [1] - PAPEL [2] - TESOURA [3]: ')
jogada2 = input('PEDRA [1] - PAPEL [2] - TESOURA [3]: ')

try:
    jogada1 = int(jogada1)
    jogada2 = int(jogada2)
except:
    print('Digite um valor válido')
    raise

valores_possiveis = [1, 2, 3]
jogada_valida = jogada1 in valores_possiveis and jogada2 in valores_possiveis

if not jogada_valida:
    print('Digite um valor possível')
    raise SystemExit

win_jogador1 = (jogada1 == 1 and jogada2 == 3) \
    or (jogada1 == 2 and jogada2 == 1) \
    or (jogada1 == 3 and jogada2 == 2)

win_jogador2 = (jogada2 == 1 and jogada1 == 3) \
    or (jogada2 == 2 and jogada1 == 1) \
    or (jogada2 == 3 and jogada1 == 2)


if jogada_valida and win_jogador1:
    print('JOGADOR 1 GANHOU')
elif jogada_valida and win_jogador2:
    print('JOGADOR 2 GANHOU')
elif (jogada1 == jogada2):
    print('EMPATE')