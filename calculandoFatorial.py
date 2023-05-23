number = int(input('Digite um numero:'))
if number == 0:
             print('O numero tem que ser maior que 0')

fatorial = number
while number != 1:
  number -= 1
  fatorial = fatorial * number
  if number == 1:
    print(f'Resultado fatorial: {fatorial}')