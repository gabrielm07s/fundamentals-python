"""
Listas de listas e seus índices
"""
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]
print(salas[0][0]) # Maria
print(salas[0][1]) # Helena
print(salas[1][0]) # Elaine
print(salas[2][0]) # Luiz
print(salas[2][1]) # João
print(salas[2][2]) # Eduarda

print(salas[2][3][4]) # acessando a tupla 

for sala in salas:
    for aluno in sala:
        print(aluno)