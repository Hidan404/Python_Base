import os
import json


__version__ = "0.1.0"
__author__ = "Ronald"
__license__ = "MIT"


linguagem_atual = os.getenv("LANG")[:5]

def leitor_var():
    """
    Função que lê o arquivo de variáveis de ambiente e imprime a linguagem atual.   
    """
    # Lê o arquivo de variáveis de ambiente
    try:
        if linguagem_atual == "pt_BR":
            print(f"linguagem atual: {linguagem_atual}")
            print("Ola Mundo")
        else:
            print(f"current language: {linguagem_atual}")
            print("Hello World")
    except Exception as e:
        print(f"An error occurred: {e}")        




if __name__ == "__main__":
    leitor_var()
