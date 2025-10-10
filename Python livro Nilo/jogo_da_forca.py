import random
import os
import json


class JogoDaForca():
    def __init__(self):
        self.digitados = []
        self.erros = 0
        self.acertos = []
        self.listas_palvras = self.ler_arquivo()
    
    def carregar_arquivo(self):
        caminho = os.path.join(os.path.dirname(__file__),"palavras_adivinhação.txt")
        return caminho    

    def ler_arquivo(self):
        caminho_arquivo = self.carregar_arquivo()
        lista_palavras = []
        with open(caminho_arquivo, "r", encoding="UTF-8") as f:
            for l in f:
                lista_palavras.extend(l.strip().split())
        print(lista_palavras)
        return lista_palavras       
    
    def nomes_pontuacoes_json(self,nome_jogador, pontos, arquivo="pontuacoes.json"):
        dados = {"nome": nome_jogador, "pontos": pontos}
        
        try:
            with open(arquivo, "r", encoding="UTF-8") as f:
                lista_pontuacao = json.load(f)
        except FileNotFoundError as f:
            print(f"Arquivo não existe {f}")       
            lista_pontuacao = []
            
        
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(lista_pontuacao, f, ensure_ascii=False,indent=4)
            
        print(f"Dados salvos {nome_jogador}")      
        
        return dados
           
    
        
        
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
    
    def jogador():
        nome_jogador = input("Digite seu nome: ").strip()
        if nome_jogador 
           

    def main(self):
        #indice_palavra = int(input("Digite um numero: "))
        #indice = (indice_palavra * 776) % len(self.listas_palvras)
        
        palavra_escolhida = random.choice(self.listas_palvras)
        rodadas = 0
        pontos = 0

        while True:
            nome_jogador = input("Digite seu nome: ").strip()
            
            
            senha = ""
            for letra in palavra_escolhida:
                senha += letra if letra in self.acertos else "."
                pontos+= 1
                
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
            self.nomes_pontuacoes_json(nome_jogador,pontos)


if __name__ == "__main__":
    jogo = JogoDaForca()
    jogo.main()
