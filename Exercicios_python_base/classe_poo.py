

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not isinstance(value, str):
            raise ValueError("O nome deve ser uma string.")
        self._nome = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        if not isinstance(value, int):
            raise ValueError("A idade deve ser um inteiro.")
        self._idade = value



pessoa1 = Pessoa("João", 30)
print(pessoa1.nome)  # Output: João
print(pessoa1.idade)  # Output: 30       