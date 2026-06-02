import math

a = float(input('Digite um valor para a:'))
b = float(input('Digite um valor para b:'))
c = float(input('Digite um valor para c:'))

delta = ((b ** 2) - (4 * a * c))
if delta < 0:
    print ('esta equação não possui raízes reais')
elif delta == 0:
    x = (-b / (2 * a))
    print('a raiz desta equação é:', x)
else:
    sqrt_d = math.sqrt(delta)
    x1 = ((-b + sqrt_d) / (2 * a))
    x2 = ((-b - sqrt_d) / (2 * a))
    
    if x1 > x2:
        x1, x2 =  x2, x1
    print('as raízes da equação são:', x1, 'e', x2)
    