import random

class AlienigenaEsconde:
    def __init__(self):
        self.vida = 100
        self.numero_aleatorio = random.randint(1, 50)
        self.niveis = ["Facil", "Medio", "Dificil"]
        self.MAX_TENTATIVAS = 0
        self.alcance_dano = (5, 20)  # será definido conforme dificuldade

    def escolher_dificuldade(self):
        while True:
            escolha = input(f"Escolha o nível ({', '.join(self.niveis)}): ").capitalize()
            if escolha in self.niveis:
                if escolha == "Facil":
                    self.MAX_TENTATIVAS = 8
                    self.alcance_dano = (5, 15)
                elif escolha == "Medio":
                    self.MAX_TENTATIVAS = 6
                    self.alcance_dano = (10, 20)
                elif escolha == "Dificil":
                    self.MAX_TENTATIVAS = 5
                    self.alcance_dano = (15, 30)
                return escolha
            else:
                print("❌ Nível inválido, tente novamente!")

    def subtrair_vida(self):
        dano = random.randint(*self.alcance_dano)
        self.vida -= dano
        return self.vida, dano

    def main(self):
        print("👽 Ache o Alien - Game 👽")
        dificuldade = self.escolher_dificuldade()
        print(f"🎮 Você escolheu o nível: {dificuldade}")

        while self.MAX_TENTATIVAS > 0 and self.vida > 0:
            tentativa = int(input("Digite uma tentativa (1 a 50): "))

            if tentativa == self.numero_aleatorio:
                print(f"🎉 Parabéns {tentativa} == {self.numero_aleatorio} | Vida: {self.vida}")
                break
            elif tentativa > self.numero_aleatorio:
                vida_atual, dano = self.subtrair_vida()
                print(f"🔼 Sua tentativa é maior que o número! | Vida: {vida_atual} | Dano: {dano}")
            else:
                vida_atual, dano = self.subtrair_vida()
                print(f"🔽 Sua tentativa é menor que o número! | Vida: {vida_atual} | Dano: {dano}")

            self.MAX_TENTATIVAS -= 1
            print(f"Tentativas restantes: {self.MAX_TENTATIVAS}")

        if self.vida <= 0 or self.MAX_TENTATIVAS == 0:
            print(f"💀 Você perdeu! O alien estava escondido no número {self.numero_aleatorio}")


if __name__ == "__main__":
    alien = AlienigenaEsconde()
    alien.main()
