"""
Repetição While (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop infinito - quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')

# Outro exemplo utilizando contador
contador = 0

while contador < 10:
    print(contador)
    contador += 1