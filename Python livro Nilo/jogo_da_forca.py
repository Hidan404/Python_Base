import random

class JogoDaForca():
    def __init__(self):
        self.digitados = []
        self.erros = 0
        self.acertos = []
        self.listas_palvras = ["painel", "python", "programa", "jogo", "forca", "desafio"]

    def boneco(self):
        estagios = [
            """
            
            

            
            
            """,  # 0 erros
            """
            |
            |
            |
            |
            """,  # 1 erro
            """
            +---+
            |
            |
            |
            |
            """,  # 2 erros
            """
            +---+
            |   O
            |
            |
            |
            """,  # 3 erros
            """
            +---+
            |   O
            |   |
            |
            |
            """,  # 4 erros
            """
            +---+
            |   O
            |  /|\\
            |
            |
            """,  # 5 erros
            """
            +---+
            |   O
            |  /|\\
            |  / \\
            |
            """,  # 6 erros (game over)
        ]
        return estagios[self.erros]
                

    def main(self):
        #indice_palavra = int(input("Digite um numero: "))
        #indice = (indice_palavra * 776) % len(self.listas_palvras)
        palavra_escolhida = random.choice(self.listas_palvras)

        while True:
            senha = ""
            for letra in palavra_escolhida:
                senha += letra if letra in self.acertos else "."
            print(senha)

            if senha == palavra_escolhida:
                print(f"Vc Acertou a palavra era {senha}")
                break

            tentativa = input("Digite uma letra: ").lower().strip()

            if tentativa in self.digitados:
                print("Vc ja idgitou essa letra")
                continue
            else:
                self.digitados.append(tentativa)
                if tentativa in palavra_escolhida:
                    self.acertos.append(tentativa)
                else:
                    self.erros += 1
                    print("Vc Errou")
                    if self.erros == 6:
                        print("Vc Perdeu")
                        print(f"A palavra era {palavra_escolhida}")
                        break

            boneco_forca = self.boneco()    
            print(boneco_forca)


if __name__ == "__main__":
    jogo = JogoDaForca()
    jogo.main()
