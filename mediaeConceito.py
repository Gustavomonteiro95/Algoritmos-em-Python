nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
if media >= 9 and media <= 10:
  print(f'Conceito A \nMédia:{media}')
if media >= 7.5 and media < 9:
  print(f'Conceito B \nMédia:{media}')
if media >= 6 and media < 7.5:
  print(f'Conceito C \nMédia:{media}')
if media >= 4 and media < 6:
  print(f'Conceito D \nMédia:{media}')
if media > 0 and media < 4:
  print(f'Conceito E \nMédia:{media:.1f}')