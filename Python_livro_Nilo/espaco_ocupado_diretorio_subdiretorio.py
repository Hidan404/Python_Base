from pathlib import Path
import sys


def bytes_mb(valor):
    return round(valor / (1024 * 1024))

def espaco_ocupado_diretorio():
    total =0

    for raiz, diretorios, arquivos in Path(sys.argv[1]).walk():
        for nome_arquivo in arquivos:
            caminho = Path(raiz, nome_arquivo)
            if Path.exists(caminho):
                total+= caminho.stat().st_size()
    return total  

def path_script():
    diretorio_atual = Path(__file__).parent.absolute()
    print(f"Diretório atual do script: {diretorio_atual}")
    return diretorio_atual / "relatorio_Tamanho.html"          

def hmtl():
     caminho_arquivo = path_script()

     with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Relatório de Arquivos</title></head><body>")
        f.write("<h1>Relatório de Arquivos</h1>")
        f.write("<table border='1'><tr><th>Nome do Arquivo</th><th>Tamanho (bytes)</th></tr>")
        for nome, tamanho, pastas  in zip(nomes, tamanhos, diretorios):
            f.write(f"<tr><td>{nome}</td><td>{tamanho}</td><td>{pastas}</td></tr>")
        f.write("</table></body></html>")

print(espaco_ocupado_diretorio())            
