"""
Dicionários 

Dicionários são coleções do tipo chave / valor
Dicionários são representaods por chaves {}
OBS: em algumas linguagens de programação, dicionários Python são conhecidos por mapas
OBS: 
    - Chaves e valor são separados por dois pontos 'chave:valor'
    - Tanto chave qaunto valor podem ser de qualquer tipo de dado
    - Podemos misturar tipos de dados
"""
print(type({}))

# Criando dicionários
# Forma de criar # 01 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)

# Forma de criar # 02 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)

# Acessando elementos (não são indexados)
# Forma # 01 - acessando via chave e imprime valor
print(paises['br'])
print(paises['eua'])
# print(paises['Brasil']) # se tentarmos acessar usando uma chave que não existe exibe KeyError

# Forma # 02 - acessando via get (Recomendado)
print(paises.get('br'))
print(paises.get('ru')) # Retorna None

# Definindo um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado') 
print(pais)

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado
# KeyError
"""
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f'Não encontrei o país')
"""

# verificar se contém
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) # não busca pelo valor e sim pela chave

# tuplas são interessantes para serem chaves de dicionários, pois são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.00600): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}
print(localidades, type(localidades))

# Adicionar elementos em dicionários
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita, type(receita))

# Forma # 01
receita['abr'] = 350
print(receita)

# Forma # 02
novo_dado = {'maio': 500}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# Atualizando dados em dicionários
# Forma # 01
receita['mai'] = 550
print(receita)

# Forma # 02
receita.update({'mai': 600})
print(receita)

# A forma de adicionar elementos ou atualizar dados em um dicionário é a mesma
# Em dicionários NÃO podemos ter chaves repetidas

# Remover dados em dicionários
# Forma # 01
ret = receita.pop('mar')
print(receita)
print(ret)

# É obrigatório passarmos a chave, e caso não encontre, é lançado KeyError
# O valor é retornado no momento do pop

# Formna # 02
del receita['fev']
print(receita)

# Tentar remover uma chave que não existe, lança KeyError
# Neste caso não recupera o valor removido

"""
Carrinho de compras contendo:
    Produto 1:
        - nome
        - quantidade
        - preco
    Produto 2:
        - nome
        - quantidade 
        - preco
"""
# Usando Lista
carrinho = []

produto1 = ['PS4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# Usando Tuplas
carrinho = ()

produto1 = ('PS4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# Usando Dicionários
carrinho = []

produto1 = { 'nome': 'PS4', 'quantidade': 1 ,'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Podemos adicionar ou remover produtos e em cada produto podemos ter certeza sobre cada informação

"""
for item in carrinho:
    nome, quantidade, preco = item['nome'], item['quantidade'], item['preco']
    print(f'{nome} - {quantidade}x - {preco:.2f}')
"""

# Outros métodos dos dicionários
d = dict(a=1, b=2, c=3)
print(d, type(d))

# Limpando um dicionário
d.clear() # zerando dados
print(d)

d = dict(a=1, b=2, c=3)

# Copiando um dicionário para outro
# Forma # 01 (Deep Copy)
novo = d.copy()
novo['d'] = 4
print(d)
print(novo)

# Forma # 02 (Shallow Copy)
novo = d
novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b') # Cria um dicionário com a chave 'a' e valor 'b'
print(outro, type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido') # crias a chaves da lista e atribui o valor desconhecido
print(usuario, type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)