import json
from pathlib import Path
from pprint import pprint
import requests
from requests.exceptions import HTTPError, RequestException

CAMINHO_SALVAR = Path(__file__).parent.resolve() / "dados_animes.json"


def consulta_api():
    try:
        entrada = input("Digite o ID do anime: ")
        id_anime = int(entrada)

        url = f"https://api.jikan.moe/v4/anime/{id_anime}/full"
        resposta = requests.get(url)

        resposta.raise_for_status()

        dados = resposta.json()
        return dados.get("data")

    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido.")
    except HTTPError as erro:
        if erro.response.status_code == 404:
            print(f"Anime com ID {id_anime} não foi encontrado.")
        else:
            print(f"Erro HTTP: {erro}")
    except RequestException as erro:
        print(f"Erro na requisição: {erro}")

    return None


def salvar_ou_adicionar_no_arquivo():
    dados_retorno = consulta_api()


    if not dados_retorno:
        return

    if CAMINHO_SALVAR.exists() and CAMINHO_SALVAR.stat().st_size > 0:
        try:
            with open(CAMINHO_SALVAR, "r", encoding="utf-8") as f:
                dados_existentes = json.load(f)
                if not isinstance(dados_existentes, list):
                    dados_existentes = []
        except json.JSONDecodeError:
            dados_existentes = []
    else:
        dados_existentes = []


    novo_anime = {
        "id": dados_retorno.get("mal_id"),
        "episodios": dados_retorno.get("episodes"),
        "score": dados_retorno.get("score"),
        "rank": dados_retorno.get("rank"),
        "status": dados_retorno.get("status"),
        "title": dados_retorno.get("title"),
    }

    if any(anime.get("id") == novo_anime["id"] for anime in dados_existentes):
        print(f"O anime com ID {novo_anime['id']}  esta salvo no arquivo.")
        return

    dados_existentes.append(novo_anime)

    with open(CAMINHO_SALVAR, "w", encoding="utf-8") as f:
        json.dump(dados_existentes, f, indent=4, ensure_ascii=False)
        print(f"Anime '{dados_retorno.get('title')}' salvo com sucesso!")

    pprint(novo_anime)


if __name__ == "__main__":
    salvar_ou_adicionar_no_arquivo()
