"""
Dado um texto lido do teclado, mostre as letras distintas usadas nele (ignore espaços e use .lower()) e quantas são.
"""
texto = input('Digite um texto: ').lower().replace(" ", "")

letras_distintas = set()
for letra in texto:
    letras_distintas.add(letra)

print(f'Letras distintas: {letras_distintas}')
