from pathlib import Path

class ArquivoIterador():
    def __init__(self,nome_arquivo):
        self.caminho_arquivo = Path(__file__).absolute().parent / nome_arquivo
        self.abrir = open(self.caminho_arquivo)

    def ler_arquivo(self):
        with Path(self.caminho_arquivo).open("r") as f:
            arquivo  = f.read()
        return arquivo    

    def __iter__(self):
        return self   
    
    def __next__(self):
        linha = self.abrir.readline()
        if linha != "":
            return linha
        else:
            self.abrir.close()
            raise StopIteration



#teste = ArquivoIterador("entrada.txt")
for t in ArquivoIterador("entrada.txt"):
    print(t)