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

            

#organizar_arquivos()    



import pandas as pd
import plotly.express as px


def ler_csv(caminho):
    try:
        arquivo_csv = pd.read_csv(caminho, sep=";", encoding="utf-8")
        dados = arquivo_csv.to_dict(orient="records")
        
       
        for linha in dados:
            for chave, valor in linha.items():
                print(f"{chave}: {valor}")
                #print("-" * 20)
            print("-" * 20)

        coluna_x = arquivo_csv["nome"]
        coluna_y = arquivo_csv["peso"] 
        figura = px.bar(x=coluna_x, y=coluna_y, title="Gráfico de Barras")
        figura.show()
       
    except FileNotFoundError as f:
        print(f"Erro: {f}")
    except Exception as e:
        print(f"Erro: {e}")    


caminho_csv = Path(__file__).parent.resolve() / "dados.csv"
ler_csv(caminho_csv)        