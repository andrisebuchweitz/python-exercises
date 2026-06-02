n = int(input('Digite um número: '))

resto = 0
restoatualizado = 0
adjacente = True

while n > 0:
    resto = n % 10
    n = n // 10
    restoatualizado = n % 10
    
    if resto == restoatualizado:
        adjacente = True
        print ('sim')
        break
    elif resto != restoatualizado:
        adjacente = False
if adjacente == False:
    print ('não')