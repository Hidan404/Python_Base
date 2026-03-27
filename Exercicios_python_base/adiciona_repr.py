def adicionsa_repr(cls):
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = ', '.join(f"{key}={value!r}" for key, value in class_dict.items())
        return class_repr
    
    cls.__repr__ = __repr__
    return cls

class MeureprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = ', '.join(f"{key}={value!r}" for key, value in class_dict.items())
        return f"{class_name}({class_repr})"
    
@adicionsa_repr
class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def lista_pessoas(self):
        lista = []
        while True:
            nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
            if nome.lower() == 'sair':
                break
            idade = input("Digite a idade da pessoa: ")
            lista.append({'nome': nome, 'idade': idade})
        return lista


if __name__ == '__main__':
    pessoa = Pessoa("João", 30)
    print(pessoa.lista_pessoas())    