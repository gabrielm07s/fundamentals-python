"""
Leia um valor em reais e mostre quantos dólares é, dada uma cotação digitada pelo usuário.
"""
valor_reais = input('Digite um valor em reais: ')
cotacao = input('Digite a cotação do dólar hoje: ')

try:
    valor_reais = float(valor_reais)
    cotacao = float(cotacao)
except:
    print('Digite um valor válido')
    raise

valor_dolares = valor_reais / cotacao

print(f'R$ {valor_reais} equivale a U$ {valor_dolares:.2f}')