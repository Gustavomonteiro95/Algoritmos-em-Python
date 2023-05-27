nome = str(input()).strip().upper()

print(nome)

inverso = ''.join(reversed(nome))

print(inverso)

if nome == inverso:
  print('Palindromo')
else:
  print('Não palíndromo')