"""
🔹 Exercício 1 – Verificar arquivos de configuração

👉 Crie um script que:

Pergunte ao usuário o nome de um arquivo (ex: config.json).

Use pathlib.Path para verificar se o arquivo existe no diretório atual.

Mostre uma mensagem dizendo se ele existe ou não.

💡 Utilidade real: quando você quer conferir se um arquivo de configuração está no lugar certo.
"""

from pathlib import Path


def perguntar_arquivo():
    # pega o caminho do diretório atual do script
    diretorio_atual = Path(__file__).parent.absolute()
    print(f"Diretório atual do script: {diretorio_atual}")

    nome_arquivo = input("Digite o nome do arquivo (ex: config.json): ").strip()
    caminho_arquivo = diretorio_atual / nome_arquivo
    print(f"Caminho completo do arquivo: {caminho_arquivo}")

    if caminho_arquivo.exists():
        print(f"O arquivo '{nome_arquivo}' existe no diretório atual.")
        caminho_arquivo.unlink() # remove o arquivo criado para teste
    else:
        print(f"O arquivo '{nome_arquivo}' NÃO existe no diretório atual.")

if __name__ == "__main__":
    perguntar_arquivo()