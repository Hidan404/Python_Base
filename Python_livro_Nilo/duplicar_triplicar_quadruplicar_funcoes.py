def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


print(criar_multiplicar(2)(2))