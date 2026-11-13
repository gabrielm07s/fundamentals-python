"""
dir, hasattr, gtattr
"""
string = 'Luiz'
metodo = 'upper'

# dir - verificar métodos de tal variável
# print(dir(string))

# verificar se tem o método
if hasattr(string, metodo):
    print('Exste upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)