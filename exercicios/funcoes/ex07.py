"""
Crie potencia(base, expoente=2). 
Chame-a com 1 argumento, com 2 argumentos e com o nome do parâmetro (expoente=3).
"""
def potencia(base, expoente=2):
    return base ** expoente

print(potencia(2))
print(potencia(2, 3))
print(potencia(base=10, expoente=3))