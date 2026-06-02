print("Bem-vindo ao jogo do NIM! Escolha:\n")

print("1 - para jogar uma partida isolada", "\n2 - para jogar um campeonato")

x = int(input())

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada: "))
    
    restam = n
    jogador = 1

    def usuario_escolhe_jogada(n, m):

        while True:
            peças_retiradas = int(input("Quantas peças você vai tirar? "))

            if peças_retiradas > m or peças_retiradas <= 0:
                print("\nOops! Jogada inválida! Tente de novo.\n")
            else:
                return n - peças_retiradas
        
    def computador_escolhe_jogada(n,m):
        if n == m:
            peças_retiradas = m
        elif n > m:    
            peças_retiradas = (n % (m + 1))
        else:
            peças_retiradas = n 
        return n - peças_retiradas
            
    if n % (m + 1) != 0:
        jogador = 1
        print("\nComputador começa!\n")        
    else:
        jogador = 0
        print("Você começa!")

    while n > 0:
        if jogador == 1:
            n = computador_escolhe_jogada(n, m)
            retirada = restam - n
            print("O computador retirou", retirada, "peça." if retirada == 1 else "peças.")
            print("Agora restam" if n > 1 else "Agora resta apenas uma", n, "peças no tabuleiro.\n" if n > 1 else "peça no tabuleiro.\n")
            if n == 0:
                print("Fim do jogo! O computador ganhou!!")
            else:
                jogador = 0        
        else:
            n = usuario_escolhe_jogada(n, m)
            retirada = restam - n
            print("\nO jogador retirou", retirada, "peça." if retirada == 1 else "peças.")
            print("Agora restam" if n > 1 else "Agora resta apenas uma", n, "peças no tabuleiro.\n" if n > 1 else "peça no tabuleiro.\n")
            if n == 0:
                print("Você ganhou!!")
            else:
                jogador = 1
        restam = n
    
    return n, m


def campeonato():

    n, m = partida()
    return n, m

if x == 2:
    print("Você escolheu um campeonato! \n")
    for i in range(3):

        print()
        print("**** Rodada", i + 1, "****\n")

        campeonato()
    print("**** Final do campeonato! ****", "\n\nPlacar: Você 0 X 3 Computador\n")
elif x == 1:
    print("Você escolheu uma partida isolada \n")
    partida()
