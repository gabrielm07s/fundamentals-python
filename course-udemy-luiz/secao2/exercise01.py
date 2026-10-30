perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

acertos = 0
for p in perguntas:
    pergunta, opcoes, resposta = p.values()

    print(f'Pergunta: {pergunta} ')
    
    print(f'\nOpções: ')
    for i in range(len(opcoes)):
        print(f'{i}) {opcoes[i]}')

    op = int(input('Escolha uma opção: '))

    if resposta == opcoes[op]:
        print('Parabéns! Você acertou!')
        acertos += 1
    else:
        print('Você errou!')

    print()

print(f'Você acertou {acertos} de {len(perguntas)} perguntas')