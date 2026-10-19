"""
Leia o lado de três segmentos e diga se formam um triângulo (cada lado < soma dos outros dois) e 
qual tipo: equilátero, isósceles ou escaleno.
"""
n1 = input('Digite o valor do 1º lado do segmento: ')
n2 = input('Digite o valor do 2º lado do segmento: ')
n3 = input('Digite o valor do 3º lado do segmento: ')

try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
except:
    print('Digite um número válido')
    raise

existe_triangulo = (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2)
triangulo_escaleno = (n1 != n2) and (n2 != n3) and (n1 != n3)
triangulo_equilatero = (n1 == n2) and (n2 == n3) and (n1 == n3)
triangulo_isoceles = (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2) or (n2 == n3 and n2 != n1)

if existe_triangulo and triangulo_equilatero:
    print('Triângulo EQUILÁTERO')
elif existe_triangulo and triangulo_escaleno:
    print('Triângulo ESCALENO')
elif existe_triangulo and triangulo_isoceles:
    print('Triângulo ISÓCELES')
else:
    print('Não existe triângulo')