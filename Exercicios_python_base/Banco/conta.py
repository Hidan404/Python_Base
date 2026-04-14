from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, nome, numero_conta, saldo):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor: int):
        try:
            valor = int(valor)
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro.")
            return
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor: int):
        pass
    
    @abstractmethod
    def transferir(self):
        pass


    def status(self):
        return f"Conta: {self.numero_conta}, Saldo: {self.saldo}"
    


