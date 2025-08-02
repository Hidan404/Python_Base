from inventario import Inventario
import random

class Personagem():
    def __init__(self, nome):
        self.nome = nome
        self.HP = 100
        self.nivel = 1
        self.forca = 3
        self.experiencia = 0
        self.status = "vivo"
        self.inventario = Inventario()  # Inicializa o inventário do personagem
    def atacar(self):
        if self.status == "vivo" and self.HP > 0:
            print(f"⚔️ {self.nome} ataca com força {self.forca}.")
        else:
            print(f"❌ {self.nome} não pode atacar porque está {self.status}.")


        
    def usar_item(self):
        self.inventario.listar_itens()

        escolha_item = input("Escolha o item pelo número:  ")
        try:
            indice = int(escolha_item) - 1
            item = self.inventario.obter_item_por_indice(indice)
            if item and item.quantidade > 0:
                if item.tipo == "poção":
                    self.HP += item.poder
                    print(f"✅ Você usou {item.nome}. HP aumentado para {self.HP}.")
                elif item.tipo == "arma":
                    self.forca += item.poder
                    print(f"✅ Você equipou {item.nome}. Força aumentada para {self.forca}.")
                elif item.tipo == "armadura":
                    self.HP += item.poder
                    print(f"✅ Você equipou {item.nome}. HP aumentado para {self.HP}.")
            else:
                print("❌ Item não encontrado ou esgotado.")
            # Reduz a quantidade do item usado  
            if item:
                if item.quantidade > 0:
                    item.quantidade -= 1
                    print(f"✅ Você usou {item.nome}.")
                    return f"HP atual: {self.HP}, Força: {self.forca}"
                else:
                    print("❌ Item esgotado.")
            else:
                print("❌ Item não encontrado.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, insira um número válido.")


    def fugir(self):
        try:
            escolha = input("Você deseja fugir? (s/n): ").lower()
            if escolha == 's':
                numero = random.randint(1, 10)
                if numero <= 5:
                    print(f"🚪 {self.nome} conseguiu fugir com sucesso!")
                else:
                    print(f"❌ {self.nome} não conseguiu fugir e foi atingido!")
                    self.HP -= 10
                    if self.HP <= 0:
                        self.status = "morto"
                        print(f"💀 {self.nome} foi derrotado!")
        except ValueError:
            print("❌ Entrada inválida. Por favor, insira 's' ou 'n'.")               
        
    def visualizar_status(self):
        print(f"👤 {self.nome} - HP: {self.HP}, Nível: {self.nivel}, Força: {self.forca}, Experiência: {self.experiencia}, Status: {self.status}")    

    def sair_do_jogo(self):
        print(f"👋 {self.nome} saiu do jogo. Até a próxima aventura!")     


    def receber_dano(self, dano):
        self.HP -= dano
        if self.HP <= 0:
            self.status = "morto"
            print(f"💀 {self.nome} foi derrotado!")
        else:
            print(f"👤 {self.nome} recebeu {dano} de dano. HP restante: {self.HP}.")



p: Personagem = Personagem("Hidan") 
print(p.usar_item()) 
p.usar_item()
p.usar_item()       