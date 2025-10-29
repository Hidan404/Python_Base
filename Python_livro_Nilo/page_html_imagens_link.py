import os
from pathlib import Path

def dir_atual():
    diretorio_atual = Path(__file__).resolve().parent
    return diretorio_atual

print("Diretório atual do script:", dir_atual())

def procurar_extensao(extensao):
    arquivos_encontarados = []
    for item in dir_atual().iterdir():
        if item.is_file() and item.suffix == extensao:
            arquivos_encontarados.append(item)

    return arquivos_encontarados        

def gerar_html():
    try:
        extensao = input("Digite a extensão dos arquivos que deseja procurar (ex: .txt, .py): ")
        if not extensao.startswith('.'):
            raise ValueError("A extensão deve começar com um ponto (.)")
    except ValueError as e:
        print("Erro:", e)
        return
    
    arquivos_encontrados = procurar_extensao(extensao)

    with open("extensao.html", "w") as arquivo_html:
        arquivo_html.write("<html>\n")
        arquivo_html.write("<body>\n")
        arquivo_html.write("<h1>Arquivos encontrados</h1>\n")
        arquivo_html.write("<ul>\n")

        for arquivo in arquivos_encontrados:
            arquivo_html.write(f"<li>{arquivo.name}</li>\n")

        arquivo_html.write("</ul>\n")
        arquivo_html.write("</body>\n")
        arquivo_html.write("</html>\n")

    print("Arquivo HTML gerado com sucesso: extensao.html")



if __name__ == "__main__":
    gerar_html()