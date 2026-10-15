"""
Podemos sair de loops utilizando a cláusula break
De uma maneira projetada
"""
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do bloco')

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break