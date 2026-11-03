"""
Crie eh_palindromo(texto) que ignora espaços, maiúsculas e minúsculas 
(por exemplo, "arara", "Ana" e "Anotaram a data da maratona" são palíndromos). 
Documente na docstring a regra que escolheu para acentos e pontuação.
"""
from unidecode import unidecode

def eh_palindromo(texto):
    """
    Enviamos um texto e verificamos se tal texto é um palídromo.
    Pode ser enviado textos com acentuação, pois é ignorado espaços, maiúsculas, minúsculas e acentos.
    """
    texto_formatado = unidecode(texto).lower().replace(' ', '')

    if texto_formatado == texto_formatado[::-1]:
        return True
    return False

texto = input('Digite um texto: ')
print(f"O texto '{{{texto}}}' é um palíndromo? {eh_palindromo(texto)}")
