hr = int(input('Digite a hora incial(apenas o primeiro número. ex: 12)'))
min = int(input('Digite os minutos iniciais:'))
sec = int(input('Digite os segundos'))


import datetime 

horainicio = datetime.time(hr,min,sec)
print(horainicio)

def rondas(h,m,s):

  rondahr = hr + h
  rondamin = min + m
  rondasec = sec + s

  if rondasec >= 60:
    rondasec = rondasec - 60
    rondamin = rondamin + 1

  if rondamin >= 60:
    rondamin = rondamin - 60
    rondahr = rondahr + 1

  if rondahr >= 24:
    rondahr = rondahr - 24

  horaronda = datetime.time(rondahr,rondamin,rondasec)

  print(horaronda)
  

rondas(1, 00, 00)
rondas(2, 10, 30)
rondas(4, 40, 50)
rondas(12, 5, 5)