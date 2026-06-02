segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dias = int(segundos/86400)
seg_rest1 = segundos % 86400
horas = int(seg_rest1/3600)
seg_rest2 = seg_rest1 % 3600
minutos = int(seg_rest2/60)
seg_rest3 = seg_rest2 % 60

print (dias, 'dias,', horas, 'hora,', minutos,'minutos e', seg_rest3, 'segundos')

