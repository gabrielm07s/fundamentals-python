def formata_data(data):
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setrmbro', \
             'Outubro', 'Novembro', 'Dezembro')
    dia, mes, ano = data.split('/')
    print(f'{dia} de {meses[int(mes) - 1]} de {ano}')
    

data = input('Digite uma data no formato (dd/MM/YYYY): ')
formata_data(data)