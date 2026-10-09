"""
Repetição while
Usar continue para pular uma repetição
"""
contador = 0

while contador <= 10:
    contador += 1
    print(contador)

    if contador == 4:
        continue

print('Acabou')