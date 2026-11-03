"""
Crie formatar_moeda(valor) que devolve o texto no padrão brasileiro: 1234.5 vira 'R$ 1.234,50'.
"""
def formatar_moeda(valor):
    valor = f'{valor:,.2f}'.replace('.', 'x').replace(',', '.').replace('x', ',')
    return valor

valor = float(input('Digite o valor em R$: '))
print(f'Formatando o valor R$ {valor:.2f} temos: {formatar_moeda(valor)}')