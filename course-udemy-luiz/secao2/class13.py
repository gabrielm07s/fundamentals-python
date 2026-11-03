"""
Escopo de Funções em Python
Escopo significa o local one aquele código pode atingir
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra gloval faz uma variável do escopo externo ser a mesma no escopo interno
"""
x = 1 # variável global

def escopo():
    global x # x global
    x = 10 # uma nova variável com valor 10
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    # print(y) # não existe porque não está no escopo
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)