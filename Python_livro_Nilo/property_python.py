class Foo():
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        return self._x or "Valor padrão"
    @x.setter
    def x(self, valor):
        if valor < 0:
            raise ValueError("O valor não pode ser negativo")
        self._x = valor
    

foo = Foo()
print(foo.x)  # Acessa o valor através da propriedade    
foo.x = 20    # Define um novo valor através da propriedade
print(foo.x)  # Acessa o valor atualizado através da propriedade
try:
    foo.x = -5   # Tenta definir um valor negativo, o que deve gerar um erro
except ValueError as e:
    print(e)