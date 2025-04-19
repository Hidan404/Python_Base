import dados_api
import os
import json


def clima():

    escolha = input("Escolha a cidade para consultar o clima: ")
    if escolha == "":
        escolha = "São Paulo"

    dados_api.salvar_dados_json(escolha)
    print("Dados do clima salvos com sucesso!")
    print("Status Code: 200")

    dados = os.path.abspath(__file__)
    dados = os.path.dirname(dados)
    caminho = os.path.join(dados, "dados.json")

    try:
        with open(caminho, "r") as arquivo:
            dados = json.load(arquivo)

            print(f"\n📍 Clima por hora em {escolha.title()}\n")

            for dia in dados['weather']:
                print(f"\n📅 Data: {dia['date']}\n")

                for hora in dia['hourly']:
                    hora_formatada = f"{int(hora['time'])//100:02d}:00"
                    temp = hora['tempC']
                    desc = hora['weatherDesc'][0]['value']
                    print(f"🕒 {hora_formatada} → 🌡️ {temp}°C - {desc}")
    except FileNotFoundError:        
        print("Arquivo não encontrado.")


clima()        

