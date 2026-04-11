from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, idade, nome):
        super().__init__(idade, nome)
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)    

    def listar_contas(self):
        print(f"Nome: {self.nome}")
        for conta in self.contas:
            print(f"Conta: {self.contas}")    