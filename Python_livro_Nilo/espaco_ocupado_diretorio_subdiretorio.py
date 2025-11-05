from pathlib import Path
import sys


def bytes_mb(valor):
    if valor < 1024:
        return f"{valor} B"
    elif valor < 1024**2:
        return f"{round(valor / 1024, 2)} KB"
    elif valor < 1024**3:
        return f"{round(valor / (1024**2), 2)} MB"
    elif valor < 1024**4:
        return f"{round(valor / (1024**3), 2)} GB"
    else:
        return f"{round(valor / (1024**4), 2)} TB"


def espaco_ocupado_diretorio():
    total =0

    for raiz, diretorios, arquivos in Path(sys.argv[1]).walk():
        for nome_arquivo in arquivos:
            caminho = Path(raiz, nome_arquivo)
            if Path.exists(caminho):
                total+= caminho.stat().st_size
    return total  

def path_script():
    diretorio_atual = Path(__file__).parent.absolute()
    print(f"Diretório atual do script: {diretorio_atual}")
    return diretorio_atual / "relatorio_Tamanho.html"          

def hmtl():
     caminho_arquivo = path_script()
     espaco_bytes = espaco_ocupado_diretorio()
     espaco_mb = bytes_mb(espaco_bytes)
    
     with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Relatório de tamanho dos arquivos</title></head><body>")
        f.write("<h1>Relatório de Tamanho em MB</h1>")
        f.write(f"<p>{espaco_mb}</p>")
        f.write("</table></body></html>")


def tui():
    hmtl()        

if __name__ == "__main__":
    tui()           
