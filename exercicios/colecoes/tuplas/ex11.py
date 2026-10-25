"""
Teste de imutabilidade: escreva um código que crie uma tupla e tente propositalmente alterar o primeiro elemento 
(tupla[0] = ...) dentro de um bloco try/except TypeError. Trate o erro e exiba uma mensagem explicativa.
"""
tupla = (0, 1, 2, 3, 4, 5)

try:
    tupla[0] = 1
except:
    print('Não é possível alterar o valor de uma tupla, pois ele é IMUTÁVEL')
    
print(tupla)