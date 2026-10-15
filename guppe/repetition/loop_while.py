"""
Loop while
Serve para iterarmos sobre sequências, diferente do for, o while pode ser usado quando não sabemos o final

while <condição>:
    <comandos>

O bloco de comandos será repetido enquanto a condição for verdadeira
Geralmente com o loop while usamos acumuladores e variáveis contadoras
"""
i = 1

while i <= 10:
    print(i, end= ' ')
    i += 1
print()
# é importanten cuidarmos do critério de parada, senão entraríamos em um loop infinito

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou? ')