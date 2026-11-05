"""
Filter

Serve para filtrar dados de uma determinada coleção
Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um interável
"""
import statistics

valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))

print(f'Média: {media:.2f}')
print(f'Valores acima da média: {list(filter(lambda valores: valores > media, valores))}')
print(f'Valore pares: {list(filter(lambda valores: valores% 2 == 0, valores))}')

# Dados coletados de algum sensor 
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
print(f'\nNovos dados coletados: {dados}')

# calculando média dos dados usando a função mean()
media = statistics.mean(dados)
print(f'Média dos valores: {media:.2f}')

res = list(filter(lambda x: x > media, dados))
print(f'Valores acima da média: {res}')

# OBS! Assim como na função map(), após serem utilizados os dados de filter(), eles são excluídos da memória

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(f'\nPaíses: {paises}')

res = list(filter(None, paises)) 
print(res)

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável
# filter() -> recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

usuarios = [
    {
        "username": "samuel",
        "tweets": ["Eu adoro bolos", "Eu adoro pizzas"],
    },
    {
        "username": "carla",
        "tweets": ["Eu amo meu gato"],
    },
    {
        "username": "jeff",
        "tweets": [],
    },
    {
        "username": "bob123",
        "tweets": [],
    },
    {
        "username": "doggo",
        "tweets": ["Eu gosto de cachorros", "Vou sair hoje"],
    },
    {
        "username": "gal",
        "tweets": [],
    },
]

# Filtrar usuários inativos no twitter
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

nomes = ['Vanessa', 'Ana', 'Maria']
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)