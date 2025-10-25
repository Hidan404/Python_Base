import os

def root_path(arquivo_nome):
    caminho = os.path.join(os.path.dirname(__file__), arquivo_nome)
    return caminho

def procurar_arquivos():
    arquivo = ["pares.txt"]
    
    
    
    lista_numeros = []
    for d in arquivo:
        caminho = root_path(d)
        if os.path.exists(caminho):
            with open(caminho, "r") as f:
                lista_numeros.extend([int(linha.strip()) for linha in f.readlines()])
    #print(lista_numeros)  
    
    lista_numeros.sort(reverse=True)   
    print(lista_numeros)   
    
    with open(root_path("pares_inversos.txt"), "w") as f:
        f.writelines(f"{n}\n" for n in lista_numeros)    

procurar_arquivos()    