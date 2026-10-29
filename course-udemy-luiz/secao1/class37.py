"""
Iterável - str, range, ...
Iterador - quem entrega o valor por vez
next - me entregue o proximo valor
iter - me entregue seu iterador
"""
nome = 'Gabriel' # iterável
iterador = iter(nome) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in nome:
    print(letra)