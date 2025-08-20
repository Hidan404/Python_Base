import sys, os
from datetime import datetime
import logging
from logging import handlers

def log_error():
    path_root = os.path.join(os.path.dirname(__file__),"infix_log.txt")
    log_formato = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename=path_root, level=logging.ERROR, format=log_formato)
    logger = handlers.RotatingFileHandler(path_root, maxBytes=1000000, backupCount=5)
    logger.setLevel(logging.ERROR)
    return logger

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
        return log_error()

def caminho_arquivo():
    path_root = os.path.join(os.path.dirname(__file__),"infix_log.txt")

    return path_root

def log_resultados(v1, v2, operacao, resultado):
    path_root = caminho_arquivo()
    tempo = datetime.now().isoformat().split(".")
    tempo_formatado = tempo[0]
    usuario = os.getenv("USER")
    with open(path_root,"a") as arquivo:
        arquivo.write(f"{tempo_formatado} - {operacao} {v1} {v2} = {resultado} - {usuario} \n")
        return arquivo
              
def ver_log(arquivo):  
    caminho = arquivo
    with open(caminho, "r", encoding="UTF-8") as f:
        print("\n*********\n")
        print(f.read())
        
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
            log = log_resultados(operacao, numero1, numero2, valor)

            caminho = caminho_arquivo()
            ver_log(caminho)

            
    except:
        error = log_error()
        return f"Erro: {error}"    
           
           
if __name__ == "__main__":
    main()           
            