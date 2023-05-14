
print('A partir do número digitado, será retornado todos os ímpares a partir de 1 até o digitado, inclusive se for negativo')

n = int(input('Digite um numero: '))
cont = 0

if n < 0:
  cont = -1
  while cont > n:
    if cont % 2 != 0:
      print(cont)
    cont -= 1
if n == 0:
  print('Nenhum número ímpar existente')
  
while cont <= n:
  if cont % 2 != 0:
    print(cont)
  cont += 1