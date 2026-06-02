import math

x1 = float(input('Digite a coordenada x do ponto 1: '))
y1 = float(input('Digite a coordenada y do ponto 1: '))
x2 = float(input('Digite a coordenada x do ponto 2: '))
y2 = float(input('Digite a coordenada y do ponto 2: '))
dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if dist >= 10:
    print('longe')
else:
    print('perto')