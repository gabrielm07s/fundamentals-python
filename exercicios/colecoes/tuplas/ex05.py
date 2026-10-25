"""
Crie uma tupla com 5 nomes de cidades. Imprima os elementos linha por linha formatados com seus respectivos índices: 
0 - São Paulo, 1 - Rio de Janeiro... usando enumerate().
"""
tupla_cidades = ('São Paulo', 'Rio de Janeiro', 'Florianopolis', 'Uberlândia', 'Araxá')

for i, valor in enumerate(tupla_cidades):
    print(f'[{i}] - {valor}')