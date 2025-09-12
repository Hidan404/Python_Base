class ContadorVogal():
    def __init(self, frase):
        self.frase = frase
        self.vogais = "AEIOUaeiou"
        self.contador = 0


    def contar_vogal(self):
        for letr5a in self.frase:
            if letra in self.vogais:
                print(letra[self.contador])    


if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    contador_vogal = ContadorVogal(frase)
    contador_vogal.contar_vogal()                