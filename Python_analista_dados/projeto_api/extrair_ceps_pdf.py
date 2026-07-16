from pypdf import PdfReader
from pathlib import Path
import re

class ExtrairTextoPDF:
    def __init__(self):
        self.caminho = Path(__file__).parent.resolve() / "NOVOS-CEPs-DE-PARAUAPEBAS.pdf"
        self.leitura = PdfReader(self.caminho)

    def extrair_texto(self):
        lista_ceps = []
        padrao_cep = re.compile(r'^\d{5}-?\d{3}$')
        for i, page in enumerate(self.leitura.pages):
            texto = page.extract_text()
            print(f"----Pagina {i}----")
            print(texto)
            texto = texto.split()
        
            lista_ceps = [cep for cep in texto if padrao_cep.match(cep)]

        return lista_ceps
    
    def salvar_ceps_txt(self):
        ceps = self.extrair_texto()
        caminho_salvar = Path(__file__).parent.resolve() / "texto_ceps.txt"
        with open(caminho_salvar, "w", encoding="utf-8") as arquivo:
            for c in ceps:
                arquivo.writelines(f"{c}\n")
            


ceps = ExtrairTextoPDF()
ceps.extrair_texto()  
ceps.salvar_ceps_txt()          