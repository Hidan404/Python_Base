class Pessoa:
    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"    