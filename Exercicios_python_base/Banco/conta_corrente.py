from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, nome, numero_conta, saldo, limite_extra):
        super().__init__(nome, numero_conta, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            print("Digite um numero inteiro")
            return
        if valor <= self.saldo:
            self.saldo-= valor
        elif valor <= self.saldo + self.limite_extra:
            self.saldo-= valor
        else:
            print("Não pode sacar") 
