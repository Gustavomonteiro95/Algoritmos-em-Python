# O Algotímo a seguir, a partir do valor de saque digitado pelo usuário irá retornar
# a quantidade de cada nota irá ser sacada.
# Ex -> R$300,00 de saque -> 3 cédulas de R$100,00, Saque de R$287 -> 2 cédulas de R$100, 1 de R$50 ,1 de R$20, 1 de R$10, 1 de R$5 e 1 de RR$2



valorSaque = int(input('Valor de saque: '))
notaCem = 0
notaCinq = 0
notaVin = 0
notaDez = 0
notaCinc = 0
notaUm = 0
if valorSaque >= 100:
  while valorSaque >= 100:
    valorSaque = valorSaque - 100
    notaCem = notaCem + 1
if valorSaque < 100 and valorSaque >= 50:
  while valorSaque < 100 and valorSaque >= 50:
    valorSaque = valorSaque - 50
    notaCinq = notaCinq + 1
if valorSaque < 50 and valorSaque >= 20:
  while valorSaque < 50 and valorSaque >= 20:
    valorSaque = valorSaque - 20
    notaVin = notaVin + 1
if valorSaque < 20 and valorSaque >= 10:
  while valorSaque < 20 and valorSaque >= 10:
    valorSaque = valorSaque - 10
    notaDez = notaDez + 1
if valorSaque < 10 and valorSaque >= 5:
  while valorSaque < 10 and valorSaque >= 5:
    valorSaque = valorSaque - 5
    notaCinc = notaCinc + 1
if valorSaque < 5 and valorSaque >= 2:
  while valorSaque < 5 and valorSaque >= 2:
    valorSaque = valorSaque - 2
    notaUm = notaUm + 1

print(notaCem, notaCinq, notaVin, notaDez, notaCinc, notaUm)