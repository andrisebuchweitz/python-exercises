n = int(input("Digite um número: "))

i = 2

if n == 1 or n == 2:
    print("primo")

elif n > 2:

    while i < n:
        
        if n % i == 0:
            
            print ("não primo")
            break
        elif n == i + 1:
            print ("primo")
        i = i + 1
