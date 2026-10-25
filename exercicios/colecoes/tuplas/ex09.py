"""
Validador de extensões: crie uma tupla com as extensões de arquivo permitidas: 
    - ('.png', '.jpg', '.jpeg', '.pdf', '.docx'). 
Peça para o usuário digitar uma extensão e informe se o arquivo é aceito ou não usando o operador in.
"""
extensoes_permitidas = ('.png', '.jpg', '.jpeg', '.pdf', '.docx')

extensao = input('Digite uma extensão: ')

if extensao in extensoes_permitidas:
    print('Arquivo é aceito')
else:
    print('Arquivo não é aceito')