"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""


from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        super().__init__()
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta     

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__()
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass  

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite_extra):
        super().__init__(agencia, numero_conta, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor):
        if valor <= self.saldo + self.limite_extra:
            self.saldo -= valor
            return True
        else:
            return False 
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
        
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente, conta):
        if cliente in self.clientes and conta in self.contas:
            return True
        else:
            return False
        

if __name__ == "__main__":
    banco = Banco("Banco XYZ")

    conta_corrente = ContaCorrente("001", "12345-6", 1000, 500)
    conta_poupanca = ContaPoupanca("001", "54321-0", 2000)

    cliente1 = Cliente("Alice", 30, conta_corrente)
    cliente2 = Cliente("Bob", 25, conta_poupanca)

    banco.adicionar_cliente(cliente1)
    banco.adicionar_cliente(cliente2)

    banco.adicionar_conta(conta_corrente)
    banco.adicionar_conta(conta_poupanca)

    # Testando autenticação e operações
    if banco.autenticar(cliente1, conta_corrente):
        print(f"{cliente1.nome} autenticado com sucesso!")
        if cliente1.conta.sacar(1200):
            print(f"Saque realizado. Saldo atual: {cliente1.conta.saldo}")
        else:
            print("Saldo insuficiente para saque.")
    else:
        print("Autenticação falhou para cliente1.")

    if banco.autenticar(cliente2, conta_poupanca):
        print(f"{cliente2.nome} autenticado com sucesso!")
        if cliente2.conta.sacar(2500):
            print(f"Saque realizado. Saldo atual: {cliente2.conta.saldo}")
        else:
            print("Saldo insuficiente para saque.")
    else:
        print("Autenticação falhou para cliente2.")        