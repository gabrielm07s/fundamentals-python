"""
Dada a tupla dos 12 meses do ano:
    - Imprima os meses do 1º semestre (fatiamento de janeiro a junho);
    - Imprima os meses do 2º semestre;
    - Imprima os meses em posições pares;
    - Imprima a lista de meses invertida usando [::-1].
"""
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro')

print(f'Meses do 1º semestre: {meses[:6]}')
print(f'Meses do 2º semestre: {meses[6:]}')
print(f'Meses em posições pares: {meses[::2]}')
print(f'Meses de maneira invertida: {meses[::-1]}')

