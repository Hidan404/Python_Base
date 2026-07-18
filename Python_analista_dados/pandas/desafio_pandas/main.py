import pandas as pd
from pathlib import Path
from google import genai
import os
from dotenv import load_dotenv
import pandas as pd
import csv

load_dotenv()

lista_perguntas = [
    "o que mensageria em programção?",
    "o que é materia escura?",
    "qual o framework mais completo em python?"
]

def salvar_perguntas(perguntas):
    caminho = Path(__file__).parent.resolve() / "perguntas.txt"
    with open(caminho, "w",encoding="utf-8") as arquivo:
        for pergunta in perguntas:
            arquivo.write(f"{pergunta}\n")

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
    
def perguntar_para_ia():
    perguntas = ler_txt()    
    modelo = "gemini-3.1-flash-lite"
    lista_respostas = {}

    cliente = genai.Client(api_key=os.getenv("CHAVE_APY"))
    for p in perguntas:
        resposta = cliente.models.generate_content_stream(
            model=modelo,
            contents=f"Resuma a resposta em poucas palavras {p}",
        )
        resposta_toda = "".join([chunk.text for chunk in resposta if chunk.text])
        lista_respostas[p] = resposta_toda

    return lista_respostas 

def transformar_resposta_em_csv(respostas):
    caminho = Path(__file__).parent.resolve() / "resposta.csv"
    with open(caminho, "w", encoding="utf-8", newline="") as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(["Perguntas", "Respostas"])
        for c, v in respostas.items():
            escrever.writerow([c,v])

salvar_perguntas(lista_perguntas)
print(ler_txt())
respostas = perguntar_para_ia()
transformar_resposta_em_csv(respostas)
