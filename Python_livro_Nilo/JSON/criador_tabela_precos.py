import json
from pathlib import Path

tabel_de_precos = {}
nome_arquivo = "preco.json"

def caminho_do_arquivo(nome):
        return Path(__file__).resolve().parent / nome
    
print("criador de tabela de preço")
while produto := input("Nome do produto: "):
    preco = int(input("Preço do produto: "))
    tabel_de_precos[produto] = preco

with Path(caminho_do_arquivo(nome_arquivo)).open("w",encoding="utf-8") as f:
    json.dump(tabel_de_precos,f,ensure_ascii=False,indent=4)