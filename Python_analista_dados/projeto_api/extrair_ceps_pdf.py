from pypdf import PdfReader
from pathlib import Path

class ExtrairTextoPDF:
    def __init__(self):
        self.caminho = Path(__file__).parent.resolve() / "NOVOS-CEPs-DE-PARAUAPEBAS.pdf"
        self.leitura = PdfReader(self.caminho)

    def extrair_texto(self):
        for i, page in enumerate(self.leitura.pages):
            texto = page.extract_text()
            print(f"----Pagina {i}----")
            print(texto)