class jogador:
    def __init__(self, nome, vida, vida_maxima, ataque, defesa, ouro, qtd_pocoes, salas_exploradas,inimigos_duplicados):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida_maxima
        self.ataque = ataque
        self.defesa = defesa
        self.ouro = ouro
        self.qtd_pocoes = qtd_pocoes
        self.salas_exploradas = salas_exploradas
        self.inimigos_encontrados = inimigos_duplicados


class Menu:
    def __init__(self):
        self.explorar = Explorar

    def menu(self):
        while True:
            print("1 - Explorar")
            print("2 - Personagem")
            print("3 - Inventario")
            print("4 - Sair")

            escolha = input("Digite uma opção: ")

            if escolha == "1":
                self.explorar.explorar()
            elif escolha == "2":
                self.mostrar_personagem()
            elif escolha == "3":
                self.mostrar_inventario()
            elif escolha == "4":
                print("Até a próxima!")
                break
            else:
                print("Opção inválida.")


class Explorar:
        def __init__(self, personagem):
            self.personagem = personagem

        def explorar(self):
            self.personagem.salas_exploradas += 1
            print(f"Você explorou a sala {self.personagem.salas_exploradas}.")

            resposta = input("Encontrou um inimigo? (s/n): ").strip().lower()
            if resposta == "s":
                nome_inimigo = input("Nome do inimigo: ").strip()
                if nome_inimigo:
                    self.personagem.inimigos_encontrados.append(nome_inimigo)
                    print(f"{nome_inimigo} foi registrado.")
            elif resposta != "n":
                print("Resposta inválida.")
       
        
