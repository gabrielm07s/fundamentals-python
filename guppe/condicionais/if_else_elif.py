"""
Estruturas Condicionais - if, else, elif

if - (se)
else - (senão)
elif - (senao se)
(podemos ter vários elif, porém else e if são apenas um)

O bloco if é executado se a condição analisada for verdadeira, o bloco else é executado se o bloco if for falso
O elif é para avaliarmos outras condições, usado para fazermos condições aninhadas

Podemos fazer diversas condições if separadas também, mas por conta de legibilidade essa estrutura é melhor e eficiente
"""
idade = 6

if idade < 18:
    print('Menor de idade')
elif (idade == 18):
    print('Possui 18 anos de idade')
else:
    print('Maior de idade')
