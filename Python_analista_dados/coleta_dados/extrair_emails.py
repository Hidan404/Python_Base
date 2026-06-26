import re
import csv
from pathlib import Path

class ExtrairEmails():
    def __init__(self):
        self.caminho_arquivo = Path(__file__).parent.resolve() / "emails.txt"
        self.emails = []

    def limpar_arquivo(self):
        with open(self.caminho_arquivo, "r", encoding="utf-8") as t:
            dados = t.readlines()    
            dados_sem_quebras = [linha.strip() for linha in dados if linha.strip() != ""]

            palavras = []
            for linha in dados_sem_quebras:
                linha_sem_virgulas = linha.replace(",", "")
                palavras.extend(linha_sem_virgulas.split())
        return palavras
    
    def extrair_emais_texto(self):
        palavras = self.limpar_arquivo()
        unir_palavras = " ".join(palavras)
        emails = re.findall(r'\S+@\S+', unir_palavras)
        return emails
    
    def salvar_csv(self):
        self.emails = self.extrair_emais_texto()
        print("E-mails encontrados:", self.emails)
        
        with open(Path(__file__).parent.resolve() / "emails.csv", "w", encoding="utf-8", newline="") as f:
            escrever_arquivo = csv.writer(f, delimiter=",")
            escrever_arquivo.writerow(["email"])
            for email in self.emails:
                escrever_arquivo.writerow([email])
        
        print(f"Arquivo salvo em: {Path(__file__).parent.resolve() / 'emails.csv'}")

# Uso:
extrator = ExtrairEmails()
extrator.salvar_csv()