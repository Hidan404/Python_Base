import sys, os
from datetime import datetime
import logging
from logging import handlers

# Função para configurar e retornar um logger de erros
def log_error():
    # Define o caminho do arquivo de log de erros
    path_root = os.path.join(os.path.dirname(__file__), "infix_log_error.txt")
    # Formato das mensagens de log
    log_formato = "%(asctime)s - %(levelname)s - %(message)s"
    # Cria um logger com nome específico
    logger = logging.getLogger("infix_error_logger")
    # Configura o nível para registrar apenas erros
    logger.setLevel(logging.ERROR)
    
    # Evitar múltiplos handlers (importante para não duplicar logs)
    if not logger.handlers:
        # Handler que rotaciona o arquivo quando atinge 1MB, mantendo 5 backups
        handler = handlers.RotatingFileHandler(path_root, maxBytes=1000000, backupCount=5)
        # Aplica o formato definido
        handler.setFormatter(logging.Formatter(log_formato))
        # Adiciona o handler ao logger
        logger.addHandler(handler)
    
    return logger

class Calculadora():
    def __init__(self, operacao_user, numero1, numero2):
        # Mapeamento de operações para métodos
        self.operacao = {
            "+": self.somar,
            "-": self.subtrair,
            "*": self.multiplicar,
            "/": self.dividir
        }
        self.operacao_usuario = operacao_user
        self.numero1 = float(numero1)
        self.numero2 = float(numero2)
        
    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2    
    
    def multiplicar(self):
        return self.numero1 * self.numero2
    
    def dividir(self):
        # Verifica divisão por zero e registra erro se necessário
        if self.numero2 == 0:
            error_log = log_error()
            error_log.error("Divisão por zero: %s / %s", self.numero1, self.numero2)
            return None
        return self.numero1 / self.numero2
    
    def executar(self):
        # Obtém a operação do dicionário
        operacao = self.operacao.get(self.operacao_usuario)
        if operacao:
            return operacao()
        else:
            # Registra erro se a operação for inválida
            error_log = log_error()
            error_log.error("Operação inválida: %s", self.operacao_usuario)
            return None

# Retorna o caminho do arquivo de log principal
def caminho_arquivo():
    return os.path.join(os.path.dirname(__file__), "infix_log.txt")

# Registra os resultados das operações no arquivo de log
def log_resultados(operacao, v1, v2, resultado):
    path_root = caminho_arquivo()
    # Obtém e formata o timestamp atual
    tempo = datetime.now().isoformat().split(".")
    tempo_formatado = tempo[0]
    # Obtém o nome do usuário (compatível com Linux e Windows)
    usuario = os.getenv("USER") or os.getenv("USERNAME") or "unknown"
    
    # Escreve no arquivo de log
    with open(path_root, "a") as arquivo:
        arquivo.write(f"{tempo_formatado} - {operacao} {v1} {v2} = {resultado} - {usuario} \n")
              
# Função para visualizar o conteúdo do arquivo de log
def ver_log(arquivo):  
    try:
        with open(arquivo, "r", encoding="UTF-8") as f:
            print("\n********* LOG *********\n")
            print(f.read())
    except FileNotFoundError:
        # Mensagem amigável se o arquivo não existir
        print("Arquivo de log não encontrado")
        
def main():
    while True:
        # Verifica se o usuário deseja continuar
        resposta = input("Deseja realizar uma operação? (s/n): ").strip().lower()
        if resposta != 's':
            print("Saindo do programa.")
            return
        try:
            # Verifica se foram passados argumentos suficientes
            if len(sys.argv) >= 4:
                operacao = sys.argv[1]
                numero1, numero2 = int(sys.argv[2]), int(sys.argv[3])
                
                # Verificar se os argumentos são números (CORREÇÃO: usar OR em vez de AND)
                if not sys.argv[2].isdigit() or not sys.argv[3].isdigit():
                    print("Numero1 e Numero2 devem ser números inteiros")
                    return
                    
            
                
                # Cria instância da calculadora
                calc = Calculadora(operacao, numero1, numero2)
                valor = calc.executar()
                
                # Se a operação foi bem sucedida, exibe e registra o resultado
                if valor is not None:
                    print(f"Resultado: {valor}")
                    log_resultados(operacao, numero1, numero2, valor)
                
                # Mostra o conteúdo do log
                caminho = caminho_arquivo()
                ver_log(caminho)
            else:
                # Mensagem de uso correto
                print("Uso: python script.py <operação> <numero1> <numero2>")
                print("Operações: +, -, *, /")
                
        except Exception as e:
            # Captura qualquer exceção não tratada e registra no log de erros
            error_log = log_error()
            # exc_info=True adiciona informações de stack trace ao log
            error_log.error("Erro ao executar a calculadora: %s", str(e), exc_info=True)
            print(f"Erro: {e}")
           
if __name__ == "__main__":
    main()