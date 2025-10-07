import os

def entrada_arquivo():
    caminho = os.path.join(os.path.dirname(__file__),"entrada.txt")
    return caminho

def main():
    with open(entrada_arquivo(), "r") as f:
        for linha in f.readlines():
            if linha[0] == ";":
                continue
            elif linha[0] == ">":
                print(f"{linha[1:].rjust(79)}")
            elif linha[0] == "*":
                print(f"{linha[1:].center(79)}")    
                
                
main()                