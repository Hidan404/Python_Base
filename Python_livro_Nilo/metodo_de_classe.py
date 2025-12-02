class Calculadora():
    def __init__(self, valor):
        self.valor = valor

    @classmethod
    def somar(cls, valor1, valor2):
        return cls(valor1 + valor2)


calc = Calculadora(5)

calc.somar(10, 20)  # Isso não altera o valor de calc.valor
calc = Calculadora.somar(10, 20)
print(calc.valor)  # Saída: 30    