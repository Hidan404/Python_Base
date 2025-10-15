import random
import os
import json


class JogoDaForca():
    def __init__(self):
        self.digitados = []
        self.erros = 0
        self.acertos = []
        self.listas_palavras = self.ler_arquivo()
        self.palavra_escolhida = ""
        self.pontos = 0
    
    def carregar_arquivo(self):
        caminho = os.path.join(os.path.dirname(__file__), "palavras_adivinhação.txt")
        return caminho    

    def ler_arquivo(self):
        caminho_arquivo = self.carregar_arquivo()
        lista_palavras = []
        try:
            with open(caminho_arquivo, "r", encoding="UTF-8") as f:
                for l in f:
                    lista_palavras.extend(l.strip().split())
            return lista_palavras
        except FileNotFoundError:
            print("Arquivo de palavras não encontrado! Usando palavras padrão.")
            return ["python", "programacao", "computador", "jogo", "forca"]
    
    def obter_nome_jogador(self):
        """
        Obtém e confirma o nome do jogador
        """
        while True:
            nome = input("\n🎮 Digite seu nome: ").strip()
            
            if not nome:
                print("❌ O nome não pode estar vazio!")
                continue
                
            print(f"\n📝 Nome digitado: {nome}")
            print("1 - ✅ Confirmar e jogar")
            print("2 - ✏️ Editar nome")
            
            opcao = input("Escolha: ").strip()
            
            if opcao == "1":
                return nome
            elif opcao == "2":
                continue
            else:
                print("Opção inválida! Digite 1 ou 2.")
    
    def nomes_pontuacoes_json(self, nome_jogador, pontos, arquivo="pontuacoes.json"):
        """
        Salva a pontuação do jogador em JSON (CORRIGIDA)
        """
        dados = {"nome": nome_jogador, "pontos": pontos}
        
        try:
            # Carregar pontuações existentes
            with open(arquivo, "r", encoding="utf-8") as f:
                lista_pontuacao = json.load(f)
        except FileNotFoundError:
            print("Arquivo não existe. Criando novo...")
            lista_pontuacao = []
        except json.JSONDecodeError:
            print("Arquivo corrompido. Criando nova lista...")
            lista_pontuacao = []
        
        # Adicionar nova pontuação à lista
        lista_pontuacao.append(dados)
        
        # Salvar lista atualizada
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(lista_pontuacao, f, ensure_ascii=False, indent=4)
            
        print(f"✅ Dados salvos: {nome_jogador} - {pontos} pontos")      
        
        return dados
    
    def mostrar_ranking(self):
        """
        Mostra o ranking de pontuações
        """
        try:
            with open("pontuacoes.json", "r", encoding="utf-8") as f:
                pontuacoes = json.load(f)
            
            # Ordenar por pontos (maior primeiro)
            pontuacoes.sort(key=lambda x: x["pontos"], reverse=True)
            
            print("\n🏆 === RANKING ===")
            for i, jogador in enumerate(pontuacoes[:10], 1):  # Top 10
                print(f"{i}º - {jogador['nome']}: {jogador['pontos']} pontos")
                
        except FileNotFoundError:
            print("\n📊 Nenhuma pontuação registrada ainda.")
    
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
    
    def calcular_pontuacao(self):
        """
        Calcula a pontuação baseada no desempenho
        """
        # Pontuação base - penaliza erros e premia acertos
        pontos_base = 100
        penalidade_erros = self.erros * 10
        bonus_letras = len(self.acertos) * 5
        
        pontuacao = max(0, pontos_base - penalidade_erros + bonus_letras)
        return pontuacao
    
    def reiniciar_jogo(self):
        """
        Reinicia as variáveis para um novo jogo
        """
        self.digitados = []
        self.erros = 0
        self.acertos = []
        self.palavra_escolhida = random.choice(self.listas_palavras)
        self.pontos = 0
    
    def main(self):
        print("=== JOGO DA FORCA ===")
        
        # Obter nome do jogador
        nome_jogador = self.obter_nome_jogador()
        
        # Escolher palavra aleatória
        self.palavra_escolhida = random.choice(self.listas_palavras).lower()
        
        print(f"\n🎯 Bem-vindo, {nome_jogador}!")
        print("A palavra tem", len(self.palavra_escolhida), "letras")
        
        while True:
            # Mostrar palavra oculta
            senha = ""
            for letra in self.palavra_escolhida:
                senha += letra if letra in self.acertos else "._"
            
            print(f"\nPalavra: {senha}")
            print(f"Letras tentadas: {', '.join(self.digitados)}")
            print(f"Erros: {self.erros}/6")
            
            # Verificar se ganhou
            if all(letra in self.acertos for letra in self.palavra_escolhida):
                self.pontos = self.calcular_pontuacao()
                print(f"\n🎉 Parabéns! Você acertou a palavra: {self.palavra_escolhida}")
                print(f"📊 Pontuação: {self.pontos}")
                
                # Salvar pontuação
                self.nomes_pontuacoes_json(nome_jogador, self.pontos)
                break
            
            # Tentativa do jogador
            tentativa = input("\nDigite uma letra: ").lower().strip()
            
            # Validar entrada
            if len(tentativa) != 1 or not tentativa.isalpha():
                print("❌ Digite apenas uma letra!")
                continue
            
            if tentativa in self.digitados:
                print("❌ Você já digitou essa letra!")
                continue
            
            # Processar tentativa
            self.digitados.append(tentativa)
            
            if tentativa in self.palavra_escolhida:
                self.acertos.append(tentativa)
                print("✅ Letra correta!")
            else:
                self.erros += 1
                print("❌ Letra errada!")
                print(self.boneco())
                
                # Verificar se perdeu
                if self.erros >= 6:
                    print(f"\n💀 Game Over! A palavra era: {self.palavra_escolhida}")
                    self.pontos = self.calcular_pontuacao()
                    print(f"📊 Pontuação final: {self.pontos}")
                    
                    # Salvar pontuação mesmo perdendo
                    self.nomes_pontuacoes_json(nome_jogador, self.pontos)
                    break
        
        # Mostrar ranking
        self.mostrar_ranking()
        
        # Perguntar se quer jogar novamente
        jogar_novamente = input("\n🔄 Deseja jogar novamente? (S/N): ").strip().upper()
        if jogar_novamente in ['S', 'SIM']:
            self.reiniciar_jogo()
            self.main()
        else:
            print("👋 Obrigado por jogar!")


if __name__ == "__main__":
    jogo = JogoDaForca()
    jogo.main() 