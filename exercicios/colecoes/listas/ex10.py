"""
Leia uma lista e diga se um valor digitado está nela (in) e, se estiver, em qual posição (index).
"""
lista = input('Digite os valores de uma lista separados por espaço: ').split()
print(lista)
valor_digitado = input('Digite um valor: ')

if valor_digitado in lista:
    posicao = lista.index(valor_digitado)
    print(f'A posição pertencente ao {valor_digitado} na lista é o de {posicao}')
else:
    print('O valor digitado não se encontra na lista')