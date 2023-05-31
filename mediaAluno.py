quantalunos = int(input('Digite a quantidade de alunos: '))

listaalunos = []

notasalunos = []

media = 0

aprovados = []
recup = []
reprovados = []
resultado = ''
cont = 0
situacao = 0


while cont < quantalunos:
      cont = cont + 1
      nome = str(input(f'Nome do aluno: '))
      listaalunos.append(nome)
      nota1 = float(input('Digite a 1ª nota do aluno: '))
      notasalunos.append(nota1)
      nota2 = float(input('Digite a 2ª nota do aluno: '))
      notasalunos.append(nota2)
      nota3 = float(input('Digite a 3ª nota do aluno: '))
      notasalunos.append(nota3)
      nota4 = float(input('Digite a 4ª nota do aluno: '))
      notasalunos.append(nota4)
      media = ((nota1 + nota2 + nota3 + nota4)/4)
      if media >= 7:
        aprovados.append(nome)
        resultado = 'Aprovado'
        print(f'{nome} teve média de {media:.2f} e a situação é de {resultado}')
      if media >= 5 and media < 7:
        recup.append(nome)
        resultado = 'Recuperação'
        situacao = (10 - media + 1)
        print(f'{nome} teve média de {media:.2f} e a situação é de {resultado}, precisando tirar {situacao:.2f} na reposição')
      if media < 5:
        reprovados.append(nome)
        resultado = 'Reprovado'
        print(f'{nome} teve média de {media:.2f} e a situação é de {resultado}')


aprv = ', '.join(aprovados)
rep = ', '.join(reprovados)
rec = ', '.join(recup)

print(f'Os alunos aprovados foram: {aprv}')
print(f'Em recuperação ficaram: {rec}')
print(f'Foram reprovados: {rep}')
