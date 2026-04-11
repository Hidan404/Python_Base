from  conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, nome, numero_conta, saldo):
        super().__init__(nome, numero_conta, saldo)

    def sacar(self, valor):
        try:
            valor = int(valor)
        except ValueError:
            print("Digite um valor inteiro")    
            return
        if valor <= self.saldo:
            self.saldo-= valor
        else:
            print("valor esta acima do saldo")   
             
