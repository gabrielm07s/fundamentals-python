"""
Crie funções que duplicam, triplicam e quadruplicam
O número recebido como parâmetros
"""
def criar_multiplicador(multiplicador):
    def multiplicar(x):
        return multiplicador * x
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

x = int(input('Digite um número: '))

print(f'Dobro: {duplicar(x)}')
print(f'Triplo: {triplicar(x)}')
print(f'Quadrúplo: {quadriplicar(x)}')