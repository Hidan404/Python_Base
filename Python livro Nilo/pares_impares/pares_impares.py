import os 

def root_path(arquivo_nome):
    caminho_root = os.path.join(os.path.dirname(__file__),arquivo_nome )
    return caminho_root

def pares():
    nome = "pares.txt"
    with open(root_path(nome), "a") as f:
        for i in range(1, 101):
            if i % 2 == 0:
                f.write(f"{i}\n")
               
            
def impares():
    nome = "impares.txt"
    with open(root_path(nome), "a") as f:
        for i in range(1, 101):
            if i % 2 != 0:
                f.write(f"{i}\n")    
                
                      
                
                
def mesclar_pares_impares():
    pares()
    impares()
    diretorio_root = os.path.dirname(os.path.abspath(__file__))
    nome_arquivos = ["pares.txt", "impares.txt"]
    total = []
    try:
        for item in nome_arquivos:
            caminho_item = os.path.join(diretorio_root, item)
            if os.path.exists(caminho_item):
                print(f"Arquivos encontrado: {item}")
                with open(caminho_item, "r") as p:
                    total.extend([int(linha.strip()) for linha in p.readlines()])
    except FileNotFoundError as files:
        print(f"Erro : {files}")     
    
    total.sort()               
    
    mesclar = "mesclar_pares_impares.txt"            
    with open(root_path(mesclar), "w") as f:
        f.writelines(f"{num}\n" for num in total)            


mesclar_pares_impares()                 