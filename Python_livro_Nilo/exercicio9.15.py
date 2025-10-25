import os

def entrada_arquivo():
    caminho = os.path.join(os.path.dirname(__file__),"entrada.txt")
    return caminho


def eliminar_espaco_repetido():
    caminho = entrada_arquivo()
    
    with open(caminho,"r") as f:
        linhas = f.readlines()
        
        with open("Saida_sem_espaco.txt", "w") as s:
            for linha in linhas:
                limpa = " ".join(linha.split())
                s.write(f"{limpa}\n")    
                
                
eliminar_espaco_repetido()                