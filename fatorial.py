n = int(input("Digite o valor de n: "))
fatorial = 1
while n > 1:
    fatorial = n * fatorial
    n = n - 1
    if n == 0:
        print (1)

print(fatorial)
