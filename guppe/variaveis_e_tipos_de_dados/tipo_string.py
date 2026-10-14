"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que estiver entre: aspas simples, aspas duplas, aspas simples triplas ou
aspas duplas triplas
"""
# mesmo que seja um número, tudo dentro de aspas é string
print('42', type('42'))
print("Olá, mundo")
print("""Hello""", type("""Hello"""))
print('''Olá''', type('''Olá'''))

nome = "Gina's Bar"
print(nome, type(nome))

# caractere de escape \n faz com que seja quebrada a linha
nome = 'Angelina \nJolie'
print(nome, type(nome))

# outra forma de quebrar a linha (usando docstrings)
nome = """Angelina
Jolie"""
print(nome, type(nome))

# para "escapar" caractere de aspas podemos usar \" ou \'
nome = "\'Angelina\""
print(nome, type(nome))

# método para deixar tudo maiúscula
nome = 'Gabriel Miranda'
print(nome.upper())

# método para deixar tudo minísculo
print(nome.lower())

# método que transforma em uma lista de strinbgs
print(nome.split())

# Fatiamento de string
print(nome[0:4]) # não é incluso o último do fatiamento, ou seja, o último é a letra que pertence ao índice 3

# ['Gabriel', 'Miranda']
print(nome.split()[0])
print(nome.split()[1])

# Inverter uma string (comeca do inicio, vai ate o ultimo e inverta)
print(nome[::-1])

# trocando
print(nome.replace('G', 'B'))