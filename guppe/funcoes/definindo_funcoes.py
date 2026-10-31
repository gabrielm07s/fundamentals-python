"""
Definindo Funções

Funções são pequenos trechos de código que realizam tarefas específicas
Pode ou não receber entradas de dados e retornar uma saída de dados
Úteis para executar procedimentos similares por repetidas vezes

OBS! Se você escrever uma função que realiza várias tarefas dentro dela
é bom verificar para que a função seja simplificada

Exemplos de funções:
- print()
- len()
- max()
- min()
- count()
- etc...
"""
# Utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']
curso = 'Programação em Python: Essencial'

# Utilizando funções integrada (Built-in) do Python print()
print(cores)
print(curso)

cores.append('roxo') # append() também é uma função
print(cores)

cores.clear()
print(cores)

# print(help(print))
# DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código 

# Definindo Funções
"""
def nome_funcao(paramentros+entrada):
    bloco_funcao

Nome da função: SEMPRE com letras minúsculas, e se for nome composto, separado por underline (snake_case)
Parâmetros de entrada: opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais 
ou não
Bloco da função: chamado de corpo da função ou implementaçlão é onde o processamento da função acontece 

OBS! Para definir uma função, utilizamos a palavra-reservada 'def' informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com ':' que é usado em Python para definir blocos
"""
# Definindo a primeira função
def diz_oi():
    print('oi')

# Utilizando funções (Chamada de Função)
diz_oi()

"""
Dentro de nossas funções podemos utilizar outras funções
Nossa função executa apenas 1 tarefa, a única coisa que ela faz é dizer oi
Não recebe nenhum parâmetro de entrada (vazio o '()')
Esta função não retorna nada

OBS! Nunca esquecer de usar os parênteses para executar uma função
"""

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()

# Em Python podemos criar variáveis do tipo de uma função e executar essa função através da variável
canta = cantar_parabens
canta()