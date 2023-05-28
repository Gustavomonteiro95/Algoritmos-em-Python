frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''inverso = junto[::-1]'''



for letra in range(len(junto)-1, -1, -1):
  inverso += junto[letra]

if inverso == junto:
  print(f'O nome {frase} é palindromo')
  print(inverso)
else:
  print(f'o nome {frase} não é palíndromo')
  print(inverso)