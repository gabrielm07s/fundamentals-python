"""
Leia o dia, mês e ano e diga se a data é válida (considere meses com 30/31 dias e fevereiro).
"""
dia = input('Digite o dia: ')
mes = input('Digite o mês: ')
ano = input('Digite o ano: ')

try:
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
except:
    print('Digite um valor válido')
    raise

ano_bissexto = (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0))
meses_31dias = [1, 3, 5, 7, 8, 10, 12]
meses_30dias = [4, 6, 9, 11]
data_invalida = ((mes > 12 or mes < 1) or (dia < 1 or dia > 31)) \
    or (dia > 30 and mes in meses_30dias) \
    or (not ano_bissexto and dia > 28 and mes == 2) \
    or (ano_bissexto and dia > 29 and mes == 2) 

if data_invalida:
    print('Data inválida')
else:
    print('Data válida')