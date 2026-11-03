"""
Crie contar_vogais(texto) que devolve a quantidade de vogais (ignore maiúsculas e acentos simples, como á).
"""
from unidecode import unidecode

def contar_vogais(*texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    qtd_vogais = {}

    for letra in texto:
        if letra in vogais:
            qtd_vogais[letra] = qtd_vogais.get(letra, 0) + 1
    
    return qtd_vogais

texto = input('Digite um texto: ')
texto_formatado = unidecode(texto).lower()
print(f'Quantidade de vogais presente: {contar_vogais(*texto_formatado)}')