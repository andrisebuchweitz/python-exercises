import math

a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

def delta(a,b,c):
    return ((b ** 2) - (4 * a * c))

def bhaskara(a,b,c):
    
    d = delta(a,b,c)
    
    if d < 0:
        print ('esta equação não possui raízes reais')
    elif d == 0:
        x = (-b / (2 * a))
        print ('a raiz desta equação é:', x)
        return x
        
    else:
        x1 = 1
        x2 = 1
        sqrt_d = math.sqrt(d)
        x1 = ((-b + sqrt_d) / (2 * a))
        x2 = ((-b - sqrt_d) / (2 * a))
        print ('as raízes da equação são:', x1, 'e', x2)
        return x1, x2        

bhaskara(a, b, c)