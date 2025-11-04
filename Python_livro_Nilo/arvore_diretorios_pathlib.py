from pathlib import Path
import sys


def arvore_diretorios():
    nome_arquivo, tamanho_arquivo, diretorios = [], [], []

    for raiz, diretorios, arquivos in Path(sys.argv[1]).walk():
        if raiz.is_dir():
            print(f"\nCaminho: {raiz}")  # Imprime o caminho atual

            # Percorre e imprime todos os subdiretórios do caminho atual
            for d in diretorios:
                print(f"  Diretório: {d}")


            # Percorre e imprime todos os arquivos do caminho atual
            for a in arquivos:
                print(f"  Arquivo: {a}")
                nome_arquivo.append(a)
                tamanho_arquivo.append(len(a))

            # Imprime um resumo com a quantidade de diretórios e arquivos encontrados
            print(f"{len(diretorios)} diretórios, {len(arquivos)} arquivos encontrados.")

            return nome_arquivo, tamanho_arquivo, diretorios
        
def path_script():
    diretorio_atual = Path(__file__).parent.absolute()
    print(f"Diretório atual do script: {diretorio_atual}")
    return diretorio_atual / "relatorio_arquivos.html"

def criar_html_nome_tamnho():
    caminho_arquivo = path_script()
    nomes, tamanhos, diretorios = arvore_diretorios()
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Relatório de Arquivos</title></head><body>")
        f.write("<h1>Relatório de Arquivos</h1>")
        f.write("<table border='1'><tr><th>Nome do Arquivo</th><th>Tamanho (bytes)</th></tr>")
        for nome, tamanho, pastas  in zip(nomes, tamanhos, diretorios):
            f.write(f"<tr><td>{nome}</td><td>{tamanho}</td><td>{pastas}</td></tr>")
        f.write("</table></body></html>")

def tui():
    criar_html_nome_tamnho()
    print("Relatório de arquivos criado com sucesso!")

if __name__ == "__main__":
    tui()          