"""
Crie eh_par(n) que devolve True ou False. Use-a para mostrar os pares de 1 a 20.
"""
def eh_par(n):
    return True if n % 2 == 0 else False

for i in range(1, 21):
    if eh_par(i):
        print(i, end= ' ')