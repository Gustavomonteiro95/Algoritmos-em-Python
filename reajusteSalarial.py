
print('O Algorítmo fará um reajuste automático com base no valor de salário digitado, com porcentagens de 20,15,10 e 5%''/n reajustado a partir da margem dos valores de sarlário:')


salarioInicial = float(input('Salario atual? '))

reajuste = 0
novoSalario = 0
percentual = 0

if salarioInicial <= 280:
  percentual = 20
  reajuste = ((salarioInicial * 20) / 100)
  novoSalario = salarioInicial + reajuste
elif salarioInicial > 280 and salarioInicial < 700:
  percentual = 15
  reajuste = ((salarioInicial * 15) / 100)
  novoSalario = salarioInicial + reajuste
elif salarioInicial > 700 and salarioInicial < 1500:
  percentual = 10
  reajuste = ((salarioInicial * 10) / 100)
  novoSalario = salarioInicial + reajuste
else:
  percentual = 5
  reajuste = ((salarioInicial * 5) / 100)
  novoSalario = salarioInicial + reajuste

  
print("Salario antes do reajuste: R$%.2f" % salarioInicial)
print("Percentual de Aumento aplicado " + str(percentual) + "%")
print("Valor do aumento: R$%.2f" % reajuste)
print("Novo salario: R$%.2f " % novoSalario)
