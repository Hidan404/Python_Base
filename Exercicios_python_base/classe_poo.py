

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

    @property #property é um decorador que transforma o método em um atributo, permitindo acessar o método como se fosse um atributo normal.
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        if not isinstance(value, int):
            raise ValueError("A idade deve ser um inteiro.")
        self._idade = value

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

aluno1 = Aluno("Maria", 20, "12345")
print(aluno1.nome)  # Output: Maria
print(aluno1.idade)  # Output: 20
print(aluno1.matricula)  # Output: 12345