import os
import os.path
from pathlib import Path

def pasta_atual():
    pasta = Path(__file__).resolve().parent
    return pasta

def verificar_dir_repetido(nome_dir):
    caminho_novo_verificar = pasta_atual() / nome_dir
    if caminho_novo_verificar.exists() and caminho_novo_verificar.is_dir():
        return True
    else:
        return False

def verificar_dir_isfile(nome_dir):
    caminho_novo_verificar = pasta_atual() / nome_dir
    if caminho_novo_verificar.exists() and caminho_novo_verificar.is_file():
        return True
    else:
        return False
        
if __name__ == "__main__":
    nome_dir = input("Digite o nome do diretório a ser verificado: ").strip()
    if verificar_dir_isfile(nome_dir):
        print(f"O nome '{nome_dir}' corresponde a um arquivo em {pasta_atual()}.")
    else:    
        if verificar_dir_repetido(nome_dir):
            print(f"O diretório '{nome_dir}' já existe em {pasta_atual()}.")
        else:
            print(f"O diretório '{nome_dir}' não existe em {pasta_atual()}.")       