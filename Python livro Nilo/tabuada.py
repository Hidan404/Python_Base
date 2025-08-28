def menu_operacoes():
    operacoes = {
        "somar": somar,
        "subtrair": subtrair,
        "multiplicar": multiplicar,
        "dividir": dividir
    }

class OperacoesTabuada:
    def __init__(self, numero):
        self.numero = numero

    def somar(self, valor):
        return self.numero + valor

    def subtrair(self, valor):
        return self.numero - valor

    def multiplicar(self, valor):
        return self.numero * valor

    def dividir(self, valor):
        if valor != 0:
            return self.numero / valor
        else:
            return "Divisão por zero não é permitida."



def gerar_tabuada():
    while True:
        numero = int(input("Digite um número para gerar a tabuada (ou -1 para sair): "))
        operacao = input("Digite a operação (somar, subtrair, multiplicar, dividir): ")
        if numero == -1:
            break
        op = OperacoesTabuada(numero)
        for i in range(1, 11):
            if operacao == "somar":
                print(f"{numero} + {i} = {op.somar(i)}")
            elif operacao == "subtrair":
                print(f"{numero} - {i} = {op.subtrair(i)}")
            elif operacao == "multiplicar":
                print(f"{numero} * {i} = {op.multiplicar(i)}")
            elif operacao == "dividir":
                print(f"{numero} / {i} = {op.dividir(i)}")


gerar_tabuada()            