from typing import Optional

class Carro:
    def __init__(self,ligado=False, cor='Branco', modelo='Sedan', velocidade=0, combustivel = 80):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade
        self.velo_maxima: int = 80
        self.combustivel = combustivel
        self.marcha = ["Re", 1, 2, 3, 4]
        self.capacidade_tanque = 100
        self.marcha_atual = 0


    def ligar(self):
        if not self.ligado and self.combustivel > 0:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")    


    def desligar(self):
        if self.ligado and self.velocidade == 0:
            self.ligado = False
            self.velocidade = 0
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")       


    def acelera(self, velocidade: int):
        if self.combustivel <= 0:
            return "Para Acelerar o combustivel ser maior que 0 "
        else:
            if self.ligado and self.velocidade <= self.velo_maxima and self.combustivel > 0:

                if self.velocidade + velocidade > self.velo_maxima:
                    self.velocidade = self.velo_maxima
                else:
                    self.velocidade += velocidade

                self.combustivel -= 5
                print(f"Acelerado em {velocidade}")
            else:
                print("Veiculo esta desligado")    


    def desacelera(self, velocidade_reducao):
        if self.ligado and self.velocidade > 0:
            if self.velocidade < velocidade_reducao:

                self.velocidade = 0
                print("Carro parou completamente")

            else:    
                self.velocidade -= velocidade_reducao
                print(f"Desacelarando em: {velocidade_reducao}")

        elif not self.ligado:
            self.velocidade = 0 
            print("veiculo esta parado")  


    def trocar_marcha(self, nova_marcha):

        if nova_marcha in self.marcha:
            self.marcha_atual = nova_marcha
            print(f"Marcha alterada para {nova_marcha}")
        else:
            print("Marcha inválida")


    def abastecer(self, litros):

        if litros <= 0:
            print("Quantidade inválida")
            return

        if self.combustivel + litros > self.capacidade_tanque:
            self.combustivel = self.capacidade_tanque
            print("Tanque cheio")
        else:
            self.combustivel += litros
            print(f"Abastecido {litros} litros")


    def status(self):

        print("\n====== STATUS DO CARRO ======")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ligado: {self.ligado}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Velocidade Máxima: {self.velo_maxima} km/h")
        print(f"Combustível: {self.combustivel}%")
        print(f"Marcha Atual: {self.marcha_atual}")
        print("=============================\n")


def mostrar_menu():
    print("\n===== SIMULADOR DE CARRO =====")
    print("1 - Ligar carro")
    print("2 - Desligar carro")
    print("3 - Acelerar")
    print("4 - Desacelerar")
    print("5 - Trocar marcha")
    print("6 - Abastecer")
    print("7 - Ver status")
    print("0 - Sair")        

def cli(cor, modelo ,ligado: Optional[bool] = None ):
    carro = Carro(ligado, cor, modelo)

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            carro.ligar()

        elif opcao == "2":
            carro.desligar()

        elif opcao == "3":
            valor = int(input("Quanto deseja acelerar? "))
            carro.acelera(valor)

        elif opcao == "4":
            valor = int(input("Quanto deseja desacelerar? "))
            carro.desacelerar(valor)

        elif opcao == "5":
            marcha = int(input("Digite a marcha: "))
            carro.trocar_marcha(marcha)

        elif opcao == "6":
            litros = int(input("Quantos litros deseja abastecer? "))
            carro.abastecer(litros)

        elif opcao == "7":
            carro.status()

        elif opcao == "0":
            print("Encerrando simulador...")
            programa_rodando = False

        else:
            print("Opção inválida")


    

if __name__ == "__main__":
    while True:
        cor = input("Digite uma cor: ")
        entrada = input("Digite True: ").lower().capitalize()
        ligado = (entrada == "True")
        modelo = input("Digite um modelo: ")

        cli(cor, modelo, ligado)

        continuar = input("Deseja continuar S/N").strip().capitalize()
        if continuar == "N":
            print("Saindo do programa...")
            break

    
    
