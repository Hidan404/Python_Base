import sys
import os

class BlocoDeNotas():
    def __init__(self, titulo, tag, texto):
        self.titulo = titulo
        self.tag = tag
        self.texto = texto
        
    def criar_arquivo(self):
        try:
            path = os.path.join(os.path.dirname(__file__), "bloco_de_notas.txt")
            with open(path, "a") as f:
                f.writelines([f"{self.titulo}\n\n", f"{self.tag}\n", f"{self.texto}\n" ]) 
                f.write("\n================\n")   
        except Exception as e:
            print(f"Erro : {e}")   
        except FileNotFoundError as f:
            print(f"Erro: {f}")  

    def ler_notas(self):
        try:
            path = os.path.join(os.path.dirname(__file__), "bloco_de_notas.txt")
            with open(path, "r") as f:
                conteudo = f.read()
                for line in conteudo.splitlines():
                    if self.titulo in line:
                        print(line)
        except Exception as e:
            print(f"Erro: {e}")

def new():
    
    if len(sys.argv) >= 3:
        try:
            comando = sys.argv[1].lower()
            titulo = sys.argv[2]
            if comando == "new":
                tag = input("Tag: ")
                texto = input("Texto: ")
                bloco_notas = BlocoDeNotas(titulo, tag, texto)
                bloco_notas.criar_arquivo()
            elif comando == "read":
                bloco_de_notas = BlocoDeNotas(titulo, None, None)
                bloco_de_notas.ler_notas()

        except Exception as e:
            print(f"Erro: {e}")        
        
if __name__ == "__main__":
    new()