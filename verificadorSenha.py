user = input('Digite o usuario:')
password = input('Digite a senha:')

if user == password:
  while user == password:
    print('A senha nao pode ser igual ao nome do usuario')
    user = input('Digite o usuario:')
    password = input('Digite a senha:')
    if user != password:
      print('Senha valida')
else:
  print('Senha valida')

  