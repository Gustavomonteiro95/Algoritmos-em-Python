num1 = float(input())
num2 = float(input())

option = int(input('Selecione uma opção \n1- par ou ímpar \n2- positivo ou negativo \n3- inteiro ou decimal'))
valueNum1 = ''
valueNum2 = ''
if option == 1:
  if num1 % 2 == 0:
    valueNum1 = 'Par'
  else:
    valueNum1 = 'Impar'
  if num2 % 2 == 0:
    valueNum2 = 'Par'
  else:
    valueNum2 = 'Impar'
  print(f'{num1} = {valueNum1}\n {num2} = {valueNum2}')
if option == 2:
  if num1 < 0:
    valueNum1 = 'Negativo'
  if num1 > 0:
    valueNum1 = 'Positivo'
  if num1 == 0:
    print('Elemento Neutro')
  if num2 < 0:
    valueNum2 = 'Negativo'
  if num2 > 0:
    valueNum2 = 'Positivo'
  if num2 == 0:
    print('Elemento Neutro')
  print(f'{num1} = {valueNum1}\n{num2} = {valueNum2}')
if option == 3:
  if num1 % 1 == 0:
    valueNum1 = 'Inteiro'
  else:
    valueNum1 = 'Decimal'
  if num2 % 1 == 0:
    valueNum2 = 'Inteiro'
  else:
    valueNum2 = 'Decimal'
  print(f'{num1} = {valueNum1} \n{num2} = {valueNum2}')
