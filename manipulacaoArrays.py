notas = []

numero = float(input())


if numero < 0 and numero > 10:
  print('Valor inválido')
  numero = float(input())

while numero >= 0 and numero <= 10 and numero != -1:
  numero = float(input())
  if numero != -1:
    notas.append(numero) 
    

quantidade = len(notas)
soma = sum(notas)
maior = max(notas)
menor = min(notas)  
inversa = []

x = len(notas) -1

for i in range(len(notas)):
  inversa.append(notas[x])
  x = x - 1

print(f'Notas:{notas}')
notas.sort()
print(f'Crescente:{notas}')
print(f'Decrescente:{inversa}')
print(f'Média:{soma/quantidade:.2f}')
print(f'Maior nota:{maior}')
print(f'Menor nota:{menor}')