diasSemana = ['Domingo', 'Segunda', ' Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
option = int(input('Digite o dia da semana (1 a 7)'))
print(f'O número {option} corresponde a {diasSemana[option-1]}')
print('O número {} corresponde a {}'.format(option, diasSemana[option-1]))