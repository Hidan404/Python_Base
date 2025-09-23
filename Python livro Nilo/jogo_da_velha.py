def tabuleiros():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return tabuleiro

def verificar_vencedor():
    def verificar_vencedor(tabuleiro):
        # Verifica linhas
        for linha in tabuleiro:
            if linha[0] == linha[1] == linha[2] and linha[0] != " ":
                return linha[0]
        # Verifica colunas
        for col in range(3):
            if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != " ":
                return tabuleiro[0][col]
        # Verifica diagonais
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
            return tabuleiro[0][0]
        if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
            return tabuleiro[0][2]
        # Verifica empate
        for linha in tabuleiro:
            if " " in linha:
                return None
        return "Empate"

def x_0():
    x, o = "X", "O"
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
        

        if verificar_vencedor():
            for linha in tabuleiro:
                print("  |".join(linha))
                print("---+---+---")
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor == "Empate":
                print("Empate!")
            else:
                print(f"O jogador {vencedor} venceu!")
            break 
        
        if jogador_inicial == " X":
            jogador_inicial = jogador2
        else:
            jogador_inicial = jogador1

           



jogo_da_velha()
       