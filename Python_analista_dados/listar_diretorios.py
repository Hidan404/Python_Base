from pathlib import Path



def listar_diretorios(caminho):
    path_diretorio = Path(caminho)
    
    for i in path_diretorio.iterdir():
        if i.is_dir():
            print(i.name)


caminho = Path(__file__).parent.parent
#print(listar_diretorios(caminho))



def organizar_arquivos():
    def limpar_caminho():
        caminho = input("Digite o caminho: ").strip().replace("'","").replace('"',"")
        try:
            pass
        except Exception as e:
            
    path = Path("/home/hidan/Documentos/")
    for item in path.iterdir():
        if item.is_file():
            extensao = item.suffix.lower().replace(".", "")
            
            if not extensao:
                extensao = "sem extensao"
            nova_pasta = path / extensao    
            print(nova_pasta)

            nova_pasta.mkdir(exist_ok=True)
            nova_pasta = nova_pasta / item.name
            item.rename(nova_pasta)

            

organizar_arquivos()    