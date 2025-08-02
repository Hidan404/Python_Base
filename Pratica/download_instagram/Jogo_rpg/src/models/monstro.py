

class Monstro():
    def __init__(self):
        self.nome = "Beholder"
        self.hp = 40
        self.forca = 5
        self.experiencia = 5
        self.status = "vivo"

    def atacar(self):
        print(f"👹 {self.nome} ataca com força {self.forca}.")
    def receber_dano(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            self.status = "morto"
            print(f"💀 {self.nome} foi derrotado!")
        else:
            print(f"👹 {self.nome} recebeu {dano} de dano. HP restante: {self.hp}.")    