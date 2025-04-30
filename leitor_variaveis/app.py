import os
import json
from translate import Translator
import sys



__version__ = "0.1.2"
__author__ = "Ronald"
__license__ = "MIT"




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
    try:
        for arg in sys.argv[1:]:
            if arg.startswith("--lang="):
                valor = arg.split("=")[1]
                argumentos["lang"] = valor
    except Exception as e:
        print(f"erro: {e}")            

    linguagem_atual = argumentos["lang"]

    if linguagem_atual is None:
        linguagem_atual = input("Digite um idiomaexemplo 'es_SP': ")

    linguagens = {
        "pt_BR": "pt",
        "en_US": "en",
        "es_SP": "es"
    }
    try:
        idioma_destino = linguagens.get(linguagem_atual)
        if idioma_destino is None:
            raise ValueError(f"Linguagem não reconhecida: {linguagem_atual}")
        
        translator = Translator(to_lang=idioma_destino)
        traduzido = translator.translate("Hello World")

        salvar_json({
            "Linguagem": linguagens[linguagem_atual],
            "Traduzido": traduzido
            })
        print(traduzido)
    except Exception as e:
        print(f"Error: {e}")        




if __name__ == "__main__":
    print(sys.argv)
    leitor_var()
