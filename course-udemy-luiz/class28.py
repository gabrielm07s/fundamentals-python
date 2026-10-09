"""
Tipos built-in (já vem com o Python não precisa instalar por fora)
Tipos vistos: str, int, float, bool
"""
string = 'Luiz Otávio'
outra_variavel = f'{string[:3]}ABC'

# string[3] = 'ABC' # tipo imutável não pode ter seu valor alterado
print(outra_variavel)

# string methods
print(string.capitalize())
print(string.zfill(20))