nome = input('Digite o usuário:')
senha = input('Digite a senha:')



if nome == senha:
  while nome == senha:
    print('Erro 589! Nome e senha não podem ser iguais!')
    nome = input('Digite o usuário:')
    senha = input('Digite a senha:')

if nome != senha:
  print('Logado com sucesso...')
