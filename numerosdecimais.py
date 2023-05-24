numero = str(input('Digite um número inteiro'))

if len(numero) >= 4:
  print(' Numero precisa ser menor que 1000')
else:
  if len(numero) == 3:
    if int(numero[0]) > 1:
      print(f'{numero} = {numero[0]} Centenas {numero[1]} dezenas {numero[2]} unidades')
    else:
      print(f'{numero} = {numero[0]} Centena {numero[1]} dezenas {numero[2]} unidades')
  if len(numero) == 2:
    print(f'{numero} = {numero[0]} dezenas {numero[1]} unidades')
  if len(numero) == 1:
    print(f'{numero} = {numero} unidade' )