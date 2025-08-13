import sys

class Calculadora():
    def __init__(self,operacao_user, numero1, numero2 ):
        self.operacao = ["+", "-", "*", "/"]
        self.operacao_usuario = operacao_user
        self.numero1 = numero1
        self.numero2 = numero2
        
    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2        
        
def main():
    try:
        if len(sys.argv) >= 4:
            operacao = sys.argv[1]
            numero1, numero2 = sys.argv[2], sys.argv[3]
            
            if not sys.argv[2].isdigit() and not sys.argv[3].isdigit():
                print("Numero1 e Numero2 tem que ser numeros")
                
    except Exception as e:
        return f"Erro: {e}"    
            