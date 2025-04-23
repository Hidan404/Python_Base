dados_pessoas = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Adicionando mais dados
dados_pessoas["profissao"] = "Engenheiro"
dados_pessoas["hobbies"] = ["leitura", "futebol", "música"]

def dicioanrio(dic: dict) -> dict:
    dados = {c: k for c, k in dic.items()}
    return dados


print(dicioanrio(dados_pessoas))