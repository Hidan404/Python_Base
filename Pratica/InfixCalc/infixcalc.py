import sys

class Calculadora():
    def __init__(self,operacao_user, numero1, numero2 ):
        self.operacao = {
            "+": self.somar,
            "-": self.subtrair,
            "*": self.multiplicar,
            "/": self.dividir
        }
        self.operacao_usuario = operacao_user # passar no terminal \* ou '*'
        self.numero1 = numero1
        self.numero2 = numero2
        
    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2    
    
    def multiplicar(self):
        return self.numero1 * self.numero2
    
    def dividir(self):
        if self.numero2 == 0:
            return
        return self.numero1 / self.numero2
    
    def executar(self):
        operacao = self.operacao.get(self.operacao_usuario)
        if operacao:
            return operacao()
        return "operacao invalida"
        
            
                
        
def main():
    try:
        
        if len(sys.argv) >= 4:
            operacao = sys.argv[1]
            numero1, numero2 = int(sys.argv[2]), int(sys.argv[3])
            
            
            if not sys.argv[2].isdigit() and not sys.argv[3].isdigit():
                print("Numero1 e Numero2 tem que ser numeros")
            
            calc = Calculadora(operacao, numero1, numero2)
            
            valor = calc.executar()
            print(valor)
            
    except Exception as e:
        return f"Erro: {e}"    
           
           
if __name__ == "__main__":
    main()           
            