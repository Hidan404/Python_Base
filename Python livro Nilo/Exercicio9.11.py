import os

def entrada_arquivo():
    caminho = os.path.join(os.path.dirname(__file__),"entrada.txt")
    return caminho

def texto_dicioanrio():
    caminho = entrada_arquivo()
    dict_palavras = {}
    
    with open(caminho, "r") as p:
        for i in p:
            palavras = i.strip().split()
            
            for palavra in palavras:
                dict_palavras[palavra.lower()] = dict_palavras.get(palavra, 0) + 1
                
    return dict_palavras            


print(texto_dicioanrio())                
                
            
            
                    