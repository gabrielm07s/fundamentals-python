"""
Funções com Parâmetros Padrão (Default Parameters)

Funções onde a passagem de parâmetros é opcional
Em Funções Python, parâmetros co valores default DEVEM estar ao final da declaração
Usando default parameters permite ser mais flexíveis nas funções, evita erros com parâmetros
incorretos e permite trabalhar com exmeplos mais legíveis de código

Podemos usar todos os tipos de dados como valores default para parâmetros
"""
print('Geek University')
print() # podemos passar algo ou não

def quadrado(numero):
    return numero ** 2

print(quadrado(2))
# print(quadrado()) # aqui o parâmetro é obrigatório

# por padrão, se não passarmos a potencia, será por padrão 2
def exponencial(numero, potencia= 2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))
print(exponencial(3))

# Se o usuário passar somente 1 parâmetro, este será atribuído ao parâmetro número, e será calculado
# o quadrado deste número
# Se o usuário passar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segudno ao parâmetro
# potência, então será calculada esta potência

# ERRO - o parâmetro default deve vir por último
# def teste(num= 2, potencia):
#     return num ** potencia

# CERTO
def teste(potencia, num= 2):
    return num ** potencia

print(teste(6))

# Outro exemplo
def soma(num1= 0, num2= 0):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

def mostra_info(nome= 'Geek', instrutor= False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_info(nome= 'Ola'))
print(mostra_info('Geek'))
print(mostra_info('Geek', instrutor= True))

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, func= soma):
    return func(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões
# Variáveis Globais
# Variáveis Locais

instrutor = 'Geek' # Variável Global

def diz_oi():
    instrutor = 'Python' # Variável Local
    return f'Oi {instrutor}'

print(diz_oi())
# OBS! Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência

def diz_oi():
    prof = 'Geek' # Variável Local
    return f'Olá {prof}'

print(diz_oi())
# print(prof) # NameError (Variável não encontrada)

# Evitar variáveis globais

total = 0
def incrementa():
    total += 1 # UnboundLocalError (variável utilziada sem ter sido inicializada)
    return total

# CORRETO
def incrementa():
    global total
    total += 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções
# Forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador # estamos usando a variável do escopo de cima
        contador += 1
        return contador
    return dentro()

print(fora())
