import requests
from pathlib import Path
from logging import basicConfig, INFO, info
import json


basicConfig(filename="erros.log", level=INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class CosumirApi:
    def __init__(self, url_formatada):
        self.url = url_formatada
        self.dados = []

    def resposta_api(self):
        try:
            resposta = requests.get(self.url, timeout=10)
            resposta.raise_for_status()
            self.dados.append(resposta.json())
            return self.dados
        except json.JSONDecodeError as e:
            info(f"Erro ao decodificar JSON: {e}")
        except requests.exceptions.InvalidURL as e:
            info(f"URL inválida: {e}")
        except Exception as e:
            info(f"Erro inesperado: {e}")
        return []

class SalvarDados:
    def __init__(self, url_formatada):
        self.caminho = Path(__file__).parent.resolve() / "dados.json"
        self.resposta = CosumirApi(url_formatada)

    def salvar_arquivo(self):
        try:
            dados_api = self.resposta.resposta_api()

            if self.caminho.exists():
                try:
                    with open(self.caminho, "r", encoding="utf-8") as f:
                        dados_existentes = json.load(f)
                except json.JSONDecodeError:
                    info("Arquivo JSON vazio ou corrompido. Criando um novo arquivo.")
                    dados_existentes = []
            else:
                dados_existentes = []

            dados_existentes.extend(dados_api)

            with open(self.caminho, "w", encoding="utf-8") as f:
                json.dump(dados_existentes, f, indent=4, ensure_ascii=False)

            print("Dados adicionados ao arquivo!")

        except IOError as e:
            info(f"Erro ao salvar arquivo: {e}")
            
    def adicioanr_dados(self, novos_dados):
        try:
            if self.caminho.exists():
                with open(self.caminho, "r", encoding="utf-8") as f:
                    dados_existentes = json.load(f)
            else:
                dados_existentes = []

            dados_existentes.append(novos_dados)

            with open(self.caminho, "w", encoding="utf-8") as f:
                json.dump(dados_existentes, f, indent=4, ensure_ascii=False)
            print("Dados adicionados com sucesso!")
        except IOError as e:
            info(f"Erro ao adicionar dados: {e}")

    def ler_arquivo(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
            print(dados)
        except IOError as e:
            info(f"Erro ao ler arquivo: {e}")

def url_formatada():
    try:
        while True:
            cep_bruto = input("Digite seu cep: ")
            cep = cep_bruto.strip().replace("-", "")

            if len(cep) == 8 and cep.isdigit():
                url = f"https://viacep.com.br/ws/{cep}/json/"
                break
            else:
                print("Erro: O CEP deve ter exatamente 8 dígitos e apenas números.")
            
        return url   
    except Exception as e:
        print(f"Erro na formatação: {e}")        

def main():
    while True:
        url = url_formatada()
        salvar_dados = SalvarDados(url)
        salvar_dados.salvar_arquivo()
        continuar = input("Deseja consultar outro CEP? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
