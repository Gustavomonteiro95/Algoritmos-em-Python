cont = 0
numero = []

quantidade = int(input('Digite quantos números serão digitados:'))

while cont < quantidade:
  numero.append(int(input()))
  cont = cont + 1

maximo = max(numero) 
minimo = min(numero)

media = (sum(numero)/quantidade) 

print(f' O maior número digitado foi: {maximo}')
print(f'O menor número digato foi {minimo}')
print(f'A média dos números foi {media:.2f}')