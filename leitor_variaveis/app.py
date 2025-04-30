import os
import json
from translate import Translator
import sys



__version__ = "0.1.2"
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
    argumentos = {
        "lang": None
    }

    for arg in sys.argv[1:]:
        if arg.startswith("--lang="):
            valor = arg.split("=")[1]
            argumentos["lang"] = valor

    linguagens = {
        "pt_BR": "pt",
        "en_US": "en",
        "es_SP": "es"
    }
    try:
        for linguagem in linguagens:
            translator = Translator(to_lang=linguagens[linguagem_atual])
            traduzido = translator.translate("Hello World")

        salvar_json({
            "Linguagem": linguagens[linguagem_atual],
            "Traduzido": traduzido
            })
        print(linguagens[linguagem_atual].translate("As variáveis de ambiente foram salvas no arquivo variaveis.json."))
    except Exception as e:
        print(f"Error: {e}")        




if __name__ == "__main__":
    print(sys.argv)
    leitor_var()
