"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado
Todo argumento que tiver um valor padrão, todos os próximos devem ter o valor padrão 
também
"""
# Refatorar -> editar o seu código
def soma(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(9 ,0 ,7)