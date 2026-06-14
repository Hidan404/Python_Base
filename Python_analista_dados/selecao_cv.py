from pathlib import Path
from typing import Optional



def caminho_usuario(caminho) -> Optional[Path]:
    try:
        caminho_ = Path(caminho)
        if caminho_.exists() and caminho_.is_dir():
            return caminho_
        print("Caminho não e um diretorio ou esta correto")
        return None
    except (TypeError, ValueError):
        print("Erro caminho e invalido")
        return None

def mover_cvs( caminho_usuario):
    caminho_criar = "/home/hidan/Cvs"
    caminho_mover_cvs = Path(caminho_criar)
    
    caminho_mover_cvs.mkdir(parents=True,exist_ok=True)
    arquivos_listados = listar_arquivos(caminho_usuario)

    for arq in arquivos_listados:
        arquivos_destino = gerar_nomes_cv_sem_colisao(caminho_mover_cvs, arq)
        arq.rename(arquivos_destino)
        print(f"Arquivos {arq.name} movidos com sucesso")


def gerar_nomes_cv_sem_colisao(oasta_destino: Path, arquivo_origem: Path):
    arquivo_base_nome = arquivo_origem.stem
    arquivo_extensao = arquivo_origem.suffix

    caminho_novo = oasta_destino / arquivo_origem.name
    contador = 1
    while caminho_novo.exists():
        nome_novo = f"{arquivo_base_nome}{contador}{arquivo_extensao}"
        caminho_novo = oasta_destino / nome_novo
        contador+=1

    return caminho_novo    

def listar_arquivos(caminho_funcao):
    diretorio = caminho_usuario(caminho_funcao)

    try:
        if diretorio is None:
            print("Diretorio e invalido")
        else:    
            padrao = "*[cC][vV]*.pdf"
            return list(diretorio.rglob(padrao))
    except Exception as e:
        print(f"Erro: {e}")

listar = Path("/home/hidan/Downloads")
mover_cvs(listar)