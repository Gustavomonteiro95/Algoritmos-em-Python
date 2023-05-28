def somaimposto (taxa,custo):
  taxa = taxa / 100
  acrescimo = custo * taxa
  novovalor = custo + acrescimo

  print(f'O novo valor será de: R${novovalor:.2f}')


t = float(input('Digite a taxa do imposto: '))
c = float(input('Digite o custo do item: '))

somaimposto(t,c)