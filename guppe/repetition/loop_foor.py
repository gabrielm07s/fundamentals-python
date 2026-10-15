"""
Estruturas de Repetição - for
Loop é uma estrutura de repetição e for é uma delas

for item in iteravel:
    # execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
"""
nome = 'Gabriel Miranda'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)

for item in lista:
    print(item)

"""
O range funciona:
range(valor_inicial, valor_final, incremento)

O valor final não é inclusivo
"""
for numero in numeros:
    print(numero)

"""
Enumerate é um par de valores, sendo o primeiro o índice e o segundo o valor
"""
for indice, valor in enumerate(nome):
    print(nome[indice])

# quando colocamos "_" é quando queremos descartar um valor, se não quisermos um valor só colocar com "_"

qtd = int(input('Quantas vezes esse loop deve rodar? '))

soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num

print(f'A soma é {soma}')

for letra in nome:
    print(letra, end= '')