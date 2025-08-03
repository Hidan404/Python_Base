from  src.models.personagem import Personagem
from models.monstro import Monstro
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
                break







   