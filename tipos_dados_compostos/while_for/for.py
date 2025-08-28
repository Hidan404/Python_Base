import os


def path_root():
    caminho = os.path.join(os.path.dirname(__file__), "texto.txt")
    return caminho

dados = {}
with open(path_root(), "r") as file:
    for linha in file:
        if ":" in linha:
            key, value = linha.split(":", 1)
            dados[key.strip()] = value.strip()
print(dados)