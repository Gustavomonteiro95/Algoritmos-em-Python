numero = int(input())
cont = 0

for i in range(1, numero + 1):
  if numero % i == 0:
    cont = cont + 1
if cont == 2:
    print(f'Primo, pois {numero} foi dividido {cont} vezes')
else:
    print(f'Não primo, pois {numero} foi divido {cont} vezes ')