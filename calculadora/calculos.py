import math


class Calculadora():
    def __init__(self):
        self.resultado = 0

    def sumar(self, *args):
        self.resultado = sum(args)
        return self.resultado

    def restar(self, *args):
        if len(args) < 2:
            raise ValueError("numero de argumentos insuficiente para subtrair.")
        resultado = args[0]
        for n in args[1:]:
            resultado -= n
        self.resultado = resultado
        return self.resultado

    def multiplicar(self, *args):
        resultado = args[0]
        for n in args[1:]:
            resultado *= n
        self.resultado = resultado
        return self.resultado

    def dividir(self, *args):
        if len(args) < 2:
            raise ValueError("numero de argumentos insuficiente para dividir.")
        resultado = args[0]
        for n in args[1:]:
            if n == 0:
                raise ZeroDivisionError("não se pode dividir por zero.")
            resultado /= n
        self.resultado = resultado
        return self.resultado
      
    def potencia(self, *args):
        if len(args) != 2:
            raise ValueError("Se requieren exactamente dos argumentos para calcular la potencia.")
        base = args[0]
        exponente = args[1]
        self.resultado = math.pow(base, exponente)
        return self.resultado