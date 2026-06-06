from pathlib import Path
from logging import basicConfig, INFO, info


def listar_diretorios(caminho):
    path_diretorio = Path(caminho)
    
    for i in path_diretorio.iterdir():
        if i.is_dir():
            print(i.name)


caminho = Path(__file__).parent.parent
#print(listar_diretorios(caminho))



def organizar_arquivos():
    arquivos_movidos_qtd = 0


    def limpar_caminho():
        caminho = input("Digite o caminho: ").strip().replace("'","").replace('"',"")
        try:
            path = Path(caminho)
            if not path.exists():
                raise FileNotFoundError("Caminho não encontrado.")
            if not path.is_dir():
                raise NotADirectoryError("O caminho não é um diretório.")
        except Exception as e:
            print(f"Erro: {e}")
            return limpar_caminho()
        return caminho
    
    caminho_corrigido = limpar_caminho()        
    path = Path(caminho_corrigido)
    for item in path.iterdir():
        if item.is_file():
            extensao = item.suffix.lower().replace(".", "")
            
            if not extensao:
                extensao = "sem extensao"
            nova_pasta = path / extensao    
            print(nova_pasta)

            nova_pasta.mkdir(exist_ok=True)

            nova_pasta = nova_pasta / item.name
            if nova_pasta.exists():
                print(f"Arquivo {item.name} já existe em {nova_pasta.parent}. Pulando...")
                continue
            item.rename(nova_pasta)
            arquivos_movidos_qtd += 1

    print(f"Total de arquivos movidos: {arquivos_movidos_qtd}")        

            

organizar_arquivos()    



import pandas as pd


def ler_csv(caminho):
    try:
        arquivo_csv = pd.read_csv(caminho)
        print(arquivo_csv)
    except FileNotFoundError as f:
        print(f"Erro: {f}")
        