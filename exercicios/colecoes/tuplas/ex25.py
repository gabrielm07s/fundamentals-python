"""
Mini agenda imutável: monte um pequeno cadastro onde cada contato é uma tupla (id, nome, telefone). 
Permita ao usuário buscar um contato pelo id ou pelo nome, retornando os dados desempacotados ou 
uma mensagem amigável caso não seja encontrado.
"""
contatos = ()

n = input('Digite quantos contatos possui: ')

try:
    n = int(n)
except:
    print('Digite um número válido')
    raise

id = 1
for i in range(n):
    nome = input(f'Digite o nome do {i + 1}º contato: ')
    telefone = input(f'Digite o telefone do {i + 1}º contato: ')

    tupla_contato = (id, nome, telefone)
    contatos += (tupla_contato, )
    id += 1
    print()

tipo_busca = input('Deseja buscar o usuário pelo id ou pelo nome? ')

contato = None
if tipo_busca == 'id':
    id_consultar = int(input('Qual id deseja consultar? '))
    for c in contatos:
        if c[0] == id_consultar:
            contato = c
            break
elif tipo_busca == 'nome':
    nome_consultar = input('Qual nome deseja consultar? ')
    for c in contatos:
        if c[1] == nome_consultar:
            contato = c
            break

if contato:
    cid, cnome, ctel = contato
    print(f'\nID: {cid}, Contato: {cnome}, Telefone: {ctel}')
else:
    print('\nContato não encontrado na agenda.')

print(f'\nID: {contato[0]}, Contato: {contato[1]}, Telefone: {contato[2]}')
