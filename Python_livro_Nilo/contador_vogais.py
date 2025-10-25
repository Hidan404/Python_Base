class ContadorVogal():
    def __init__(self, frase):
        self.frase = frase
        self.vogais = "AEIOUaeiou"
        self.contador = ""


    def contar_vogal(self):
        for letra in self.frase:
            if letra in self.vogais:
                self.contador += letra
        print(f"A frase '{self.frase}' tem {len(self.contador)} vogais: {self.contador}")


if __name__ == "__main__":
    frase = input("Digite uma frase: ")
    contador_vogal = ContadorVogal(frase)
    contador_vogal.contar_vogal()                