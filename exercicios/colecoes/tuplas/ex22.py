"""
Distância entre dois pontos 3D: represente dois pontos no espaço através de tuplas 
p1 = (x1, y1, z1) e p2 = (x2, y2, z2). Calcule a distância euclidiana entre eles:
Utilize desempacotamento de tuplas e a biblioteca math.
"""
import math

p1 = tuple(input('Digite o ponto 1 (x1, y1, z1): ').split())
p2 = tuple(input('Digite o ponto 2 (x2, y2, z2): ').split())

x1, y1, z1 = float(p1[0]), float(p1[1]), float(p1[2])
x2, y2, z2 = float(p2[0]), float(p2[1]), float(p2[2])

distancia_euclidiana = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1)** 2) + ((z2 - z1) ** 2))

print(f'Distância euclidiana: {distancia_euclidiana:.2f}')