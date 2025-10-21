from agenda_telefones import Agenda
import os

class SalvarArquivos(Agenda):
    def __init__(self):
        super().__init__()
    
    def root_path(self,arquivo):
        root = os.path.join(os.path.dirname(__file__), arquivo)   
        return root
     
    def le(self):
        nome_arquivo = self.pede_nome_arquivo()  
        try:
            with open(self.root_path(nome_arquivo), "r") as arquivo:
                for a in arquivo.readlines():
                    nome, telefone  = a.strip().split("#")
                    self.agenda.append([nome, telefone])
        except FileNotFoundError as fnfe:
            print(f"Erro: {fnfe}")            
    
    def grava(self):
        nome_arquivo = self.pede_nome_arquivo()
        
        try:
            with open(self.root_path(nome_arquivo), "w") as f:
                for a in self.agenda:
                    f.write(f"{a[0]}#{a[1]}\n")
        except OSError as oe:
            print(f"Erro: {oe}")            
                
    def tamanho_agenda(self):
        nome_arquivo = self.pede_nome_arquivo()
        
        try:
            with open(self.root_path(nome_arquivo),"r") as f:
                contador = 0
                for i in f.readlines():
                    linha = i.strip()
                    
                    if linha:
                        contador+= 1
                        print(linha, sep=" | ")
            print(f"\n{contador}\n")                 
        except FileNotFoundError as fne:
            print(f"Erro: {fne}")
                                