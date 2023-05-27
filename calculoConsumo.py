kinitial = float(input('Qual o valor da kilometragem inicial? '))

kfinal = float(input('Qual o valor da kilometragem final? '))

qtdliters = float(input('Quantos litros foram consumidos na viagem? '))

def averageConsumption(ki,kf,ql):
	return (kf- ki) / ql


print(f'O valor do consumo médio é de: {averageConsumption(kinitial,kfinal,qtdliters):.1f} Km/L')