import requests
import os

def callerkit_lookup(number, country="BR"):
    url = "https://caller-kit.com/api/v1/search/number"
    payload = {
        "country_code": country,
        "number": number,
        "page": 1,
        "per_page": 10
    }
    

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Api-key': 'sk_0L554xUM1qOi4z0cFbmr5geejqueEkQt'
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
    except requests.RequestException as error:
        raise RuntimeError(f"Falha de conexão com a API: {error}") from error

    if response.status_code == 200:
        return response.json()

    if response.status_code >= 500:
        raise RuntimeError(
            f"A API retornou erro interno ({response.status_code}). "
            "Tente novamente mais tarde; verifique também os dados enviados."
        )

    raise RuntimeError(f"Erro da API: {response.status_code} - {response.text}")

# Exemplo de uso
try:
    result = callerkit_lookup("94984101871")
    print(result)
    print(f"Nome: {result.get('name', 'Não encontrado')}")
    print(f"Endereço: {result.get('address', 'Não encontrado')}")
except Exception as e:
    print(f"Erro: {e}")