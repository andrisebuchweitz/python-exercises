def soma(x):
    x = int(x)
    a = 0

    while x > 0:
        resto = x % 10
        x = x // 10
        a = a + resto
    return a


x = input("Digite um número inteiro: ")
print(soma(x))
