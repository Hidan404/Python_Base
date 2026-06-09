import requests
from pathlib import Path
from logging import basicConfig, INFO, info
from tqdm import tqdm
import json



class CosumirApi:
    def __init__(self, url):
        self.url = url
        self.dados = []

    def resposta_api(self):
        try:
            resposta = requests.get(self.url)
            resposta.raise_for_status()
            self.dados.append(resposta.json())
            return self.dados
        except requests.JSONDecodeError as e:
            print(f"Erro: {e}")  
        except requests.exceptions.InvalidURL as e:
            print(f"Erro: {e}")    
        except Exception as e:
            print(f"Erro: {e}")


class SalvarDados:
    def __init__(self,url ):
        self.caminho = Path(__file__).parent.resolve() / "dados.json"
        self.resposta = CosumirApi(url)

    def salvar_arquivo(self):
        with open(self.caminho, "w", encoding="utf-8") as f:
            json.dump(self.resposta.resposta_api(),f, indent=4,ensure_ascii=False)

    def ler_arquivo(self):
        with open(self.caminho, "r") as f:
            dados = json.load(f)
        print(dados)            


url = "https://viacep.com.br/ws/01001000/json/"
s = SalvarDados(url)
s.salvar_arquivo()
s.ler_arquivo()
