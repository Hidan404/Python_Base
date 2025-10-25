import os
from pathlib import Path

def dir_atual():
    diretorio_atual = Path(__file__).resolve().parent
    return diretorio_atual

print("Diretório atual do script:", dir_atual())

def procurar_extensao(extensao):
    arquivos_encontarados = []
    for item in dir_atual().iterdir():
        if item.is_file() and item.suffix == extensao:
            arquivos_encontarados.append(item)

    return arquivos_encontarados        

def gerar_html():
    arquivos_encontrados = procurar_extensao()
    