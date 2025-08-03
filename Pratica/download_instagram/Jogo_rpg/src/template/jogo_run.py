from  src.models.personagem import Personagem
from src.models.monstro import Monstro
import random


class Inicio_jogo():
    def __init__(self):
        self.personagem = Personagem("Hidan")
        self.mosntro = Monstro()
    def boas_vindas_jogo(self):
        print("🎮 Bem-vindo ao Jogo de RPG!")
        print(f"👤 Personagem: {self.personagem.nome}")
        print(f"👹 Monstro: {self.mosntro.nome}")
        print("⚔️ Prepare-se para a aventura!")    

    def inciar(self):
        self.boas_vindas_jogo()
        while True:
            if self.personagem.HP > 0:
                self.personagem.visualizar_status()
                escolha = input("Escolha uma ação: (1) Atacar (2) Usar Item (3) Fugir (4) Sair: ")
                if escolha == '1':
                    dano = self.personagem.atacar()
                    print(f"⚔️ Você atacou o {self.mosntro.nome} causando {dano} de dano.")
                    self.mosntro.receber_dano(dano)
                    if self.mosntro.status == "morto":
                        print("🎉 Você derrotou o monstro!")
                        self.personagem.experiencia += self.mosntro.experiencia
                        print(f"💎 Experiência adquirida: {self.mosntro.experiencia}. Total: {self.personagem.experiencia}")
                        if self.personagem.experiencia >= 10:
                            self.personagem.nivel += 1
                            self.personagem.forca += 2
                            print(f"🚀 Parabéns! Você subiu para o nível {self.personagem.nivel}. Força aumentada para {self.personagem.forca}.")
                        
                elif escolha == "2":
                    print(self.personagem.usar_item())
                elif escolha == "3":
                    self.personagem.fugir()
                elif escolha == "4":
                    escolha_sair = input("Você tem certeza que deseja sair? (s/n): ").lower()
                    if escolha_sair == 's':
                        self.personagem.sair_do_jogo()
                        break
                    
                        
                







   