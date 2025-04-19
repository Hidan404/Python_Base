import requests
import json
import os


def salvar_dados_json(cidade="São Paulo"):
    caminho = os.path.abspath(__file__)
    caminho = os.path.dirname(caminho)

    
    if not os.path.exists(caminho):
        os.makedirs(caminho)

        
    url = f"https://wttr.in/{cidade}?format=j1"
    resposta = requests.get(url)
    try:
        if resposta.status_code == 200:
            dadso = resposta.json()
            with open(f"{caminho}/dados.json", "w") as arquivo:
                json.dump(dadso, arquivo, indent=4)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
    else:
        print("Dados salvos com sucesso!")
        print(f"Status Code: {resposta.status_code}")
    
    



