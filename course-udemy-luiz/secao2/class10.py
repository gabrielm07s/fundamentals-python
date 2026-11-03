"""
Introdução a funções (def) em Python
Funções são trechos de códigos usados para replicar determinada ação ao longo do código
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
Por padrão, as funções Python retornam None (nada)
"""
def Print():
    print('Várias')

def imprimir(a, b, c):
    print(a, b, c)

for i in range(5):
    Print()

imprimir(1, 2, 3) 

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao()