def tabuleiros():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return tabuleiro

    

def x_0():
    x, o = "X
    return x, o

def jogo_da_velha():
    jogador1 = x_0()[0]   
    jogador2 = x_0()[1]
    jogador_inicial = jogador1
    tabuleiro = tabuleiros()
    while True:
        for linha in tabuleiro:
            print("  |".join(linha))
            print("---+---+---")

        linha = int(input("0-2: "))
        coluna = int(input("0-2: "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_inicial
        else:
            print("Digite uma opção valida")
            continue

        if jogador_inicial == "X":
            jogador_inicial = jogador2
        else:
            jogador_inicial = jogador1



jogo_da_velha()
       