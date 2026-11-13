"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: raise não é uma função, é uma palavra reservada, assim como def ou qualquer outra em Python
raise é util para que possamos criar nossas proprias execções e mensagens de erros

Sintaxe:
raise TipoDoErro('Mensagem do Erro')
raise ValueError('Valor Incorreto')

OBS! assim como o return, o raise também finaliza a função, nada após dele é executado
"""
def colorir(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')

    print(f'O texto {texto} será impresso na cor {cor}')

colorir('Geek', 'azul')