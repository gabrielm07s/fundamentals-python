"""
Crie eh_palindromo(texto) que ignora espaços, maiúsculas e minúsculas 
(por exemplo, "arara", "Ana" e "Anotaram a data da maratona" são palíndromos). 
Documente na docstring a regra que escolheu para acentos e pontuação.
"""
def eh_palindromo(texto):
    if texto == texto[::-1]:
        return True
    return False

texto = input('Digite um texto: ')
texto_formatado = texto.lower().replace(' ', '')

print(f"O texto '{{{texto}}}' é um palíndromo? {eh_palindromo(texto_formatado)}")
