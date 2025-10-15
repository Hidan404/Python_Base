from agenda_telefones import Agenda

class SalvarArquivos(Agenda):
    def __init__(self):
        super().__init__()
        
    def le(self):
        nome_arquivo = self.pede_nome_arquivo()  
        
        with open(nome_arquivo, "r") as arquivo:
            for a in arquivo.readlines():
                nome, telefone  = a.strip().split("#")
                self.agenda.append([nome, telefone])
    
    def grava(self):
        nome_arquivo = self.pede_nome_arquivo()
        
        with open(nome_arquivo, "w") as f:
            for a in self.agenda:
                f.write(f"{a[0]}#{a[1]}\n")
                            