"""
Leia uma hora (0–23) e responda Bom dia, Boa tarde ou Boa noite.
"""
hora = input('Digite uma hora: ')

try:
    hora = int(hora)
except:
    print('Digite um valor válido')
    raise

if (hora >= 0 and hora < 12):
    print('Bom dia')
elif (hora >= 12 and hora <= 18):
    print('Boa tarde')
elif (hora >= 19 and hora <= 23):
    print('Boa noite')
else:
    print('Hora não existe')