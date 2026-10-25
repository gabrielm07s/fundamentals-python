"""
Conversão e alteração: crie uma tupla com 5 cores. Mostre que não é possível alterar diretamente; 
converta-a para lista com list(), troque a cor da posição central por 'Dourado', 
adicione uma cor no final e converta novamente para tupla com tuple().
"""
cores = ('Amarelo', 'Azul', 'Verde', 'Vermelho', 'Laranja')

# cores[2] = 'Violeta'
lista_cores = list(cores)
lista_cores[len(cores) // 2] = 'Dourado'
lista_cores.append('Violeta')

cores = tuple(lista_cores)
print(cores)