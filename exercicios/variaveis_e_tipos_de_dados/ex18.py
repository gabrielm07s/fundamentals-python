"""
Leia uma quantidade de segundos e converta para horas, minutos e segundos (use // e %).
"""
qtd_segundos = input('Digite a quantidade de segundos: ')

try:
    qtd_segundos = int(qtd_segundos)
except:
    print('Digite um número válido')
    raise

horas = qtd_segundos // 3600
qtd_segundos %= 3600
minutos = qtd_segundos // 60
qtd_segundos %= 60
segundos = qtd_segundos

print(f'{horas:02d}:{minutos:02d}:{segundos:02d}')