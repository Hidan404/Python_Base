import pandas as pd
from pathlib import Path

lista_perguntas = [
    "o que mensageria em programção?",
    "o que é materia escura?",
    "qual o framework mais completo em python?"
]

def salvar_perguntas(perguntas):
    caminho = Path(__file__).parent.resolve() / "perguntas.txt"
    with open(caminho, "w",encoding="utf-8") as arquivo:
        arquivo.writelines(f"{perguntas}\n")

    return caminho

def ler_txt(nome_arquivo="perguntas.txt"):
    caminho = Path(__file__).parent.resolve() / nome_arquivo
    perguntas = []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha_limpa = linha.strip()
                if linha_limpa:  
                    perguntas.append(linha_limpa)
        return perguntas
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return []

print(ler_txt())