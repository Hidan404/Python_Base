import math


class Calculadora():
    def __init__(self):
        self.resultado = 0

    def somar(self, *args):
        self.resultado = sum(args)
        return self.resultado

    def diminuir(self, *args):
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
    
    
class View(Calculadora):
    def __init__(self):
        super().__init__()
        self.operacoes = ["somar", "diminuir", "multiplicar", "dividir", "potencia"]
        
    def obter_numeros(self):
        numeros = []
        while True:
            entrada = input("Digite um número (ou '=' para calcular): ")
            if entrada == '=':
                break
            try:
                numeros.append(float(entrada))
            except ValueError:
                print("Por favor, digite um número válido!")
        return numeros
        
    def main(self):
        while True:
            print("\n====CALCULADORA====")
            print("Operações disponíveis:")
            for i, op in enumerate(self.operacoes, 1):
                print(f"{i}. {op}")
            
            try:
                escolha_idx = int(input("Escolha uma operação (número): ")) - 1
                if 0 <= escolha_idx < len(self.operacoes):
                    escolha = self.operacoes[escolha_idx]
                else:
                    print("Opção inválida!")
                    continue
            except ValueError:
                print("Por favor, digite um número válido!")
                continue
            
            numeros = self.obter_numeros()
            
            try:
                resultado = getattr(self, escolha)(*numeros)
                print(f"\nResultado: {resultado}")
            except Exception as e:
                print(f"\nErro: {e}")
            
            continuar = input("\nDeseja continuar? (s/n): ").lower()
            if continuar != 's':
                break
        return "Calculadora encerrada."
        

        
    
if __name__ == "__main__":
    calc = View()
    print(calc.main())
        