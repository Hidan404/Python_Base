import json
from pathlib import Path

class LerArquivo():
    def __init__(self):
        self.caminho = Path(__file__).resolve().parent
        self.nome_arquivo = "dados.json"
        
    def caminho_do_arquivo(self):
        return self.caminho / self.nome_arquivo
    
    def ler_json(self):
        with open(self.caminho_do_arquivo(), "r", encoding="utf-8") as f:
            dados = json.load(f)
        if isinstance(dados, list):
            for d in dados:
                print(d)    
        if isinstance(dados,dict):        
            for chave, valor in  dados.items():
                print(f"Chave: {chave} | valor: {valor}")        
            
       
       
if __name__ == "__main__":
    ler_jason = LerArquivo()
    ler_jason.ler_json()            
            