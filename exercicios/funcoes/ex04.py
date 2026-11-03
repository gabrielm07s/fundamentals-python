"""
Crie eh_par(n) que devolve True ou False. Use-a para mostrar os pares de 1 a 20.
"""
def eh_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in range(21):
    print(f'{i} eh par? {eh_par(i)}')