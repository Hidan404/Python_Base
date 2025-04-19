import os
import json
from translate import Translator



__version__ = "0.1.0"
__author__ = "Ronald"
__license__ = "MIT"


linguagem_atual = os.getenv("LANG")[:5]

def salvar_json(dados):
    try:
        caminho = os.path.abspath(__file__)
        caminho = os.path.dirname(caminho)
        
        with open(f"{caminho}/variaveis.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"An error occurred: {e}")    


def leitor_var():
    """
    Função que lê o arquivo de variáveis de ambiente e imprime a linguagem atual.   
    """
  
    try:
        if linguagem_atual == "pt_BR":
            print(f"linguagem atual: {linguagem_atual}")
            print("Ola Mundo")
            translator = Translator(to_lang="pt")
            traduzido = translator.translate("Hello World")
            salvar_json({"language": f"linguagem atual: {linguagem_atual}", "translated": traduzido})
            
        elif linguagem_atual == "en_US":
            print(f"Liguagem atual: {linguagem_atual}")
            translator = Translator(to_lang="en")
            traduzido = translator.translate("Ola mundo")
            salvar_json({"language": f"linguagem atual: {linguagem_atual}", "translated": traduzido})
        else:
            print(f"linguagem atual: {linguagem_atual}")
            print("linguagem não suportada")
            salvar_json({"language": linguagem_atual})
    except Exception as e:
        print(f"Error: {e}")        




if __name__ == "__main__":
    leitor_var()
