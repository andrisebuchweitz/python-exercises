def eh_primo(num):

    if num < 2:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True

def maior_primo(n):

    while n >= 2:

        if eh_primo(n):
            return n

        n -= 1


print(maior_primo(200))