

class Monstro():
    def __init__(self, nivel_personagem):
        self.nome = "Beholder"
        self.hp = 40
        self.forca = 5 + (nivel_personagem * 10)
        self.experiencia = 5
        self.status = "vivo"

    def atacar(self):
        dano = self.forca
        print(f"👹 {self.nome} ataca com força {dano}.")
        return dano
    
    def receber_dano(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            self.status = "morto"
            print(f"💀 {self.nome} foi derrotado!")
        else:
            print(f"👹 {self.nome} recebeu {dano} de dano. HP restante: {self.hp}.") 
            
    def aumentar_nivel(self):
        niveis = [1,2,3,4,5] 
        if niveis:
            self.hp *= niveis[]         