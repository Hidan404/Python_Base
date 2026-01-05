from pessoa import Pessoa
from pathlib import Path
import json

class ArquivoJsonPessoa():
    def __init__(self):
        self.caminho = Path(__file__).parent.resolve() 
        self.nome_arquivo = "Pessoa.json"
        
    def caminho_completo(self):
        return self.caminho / self.nome_arquivo
    
    def dados(self):
        
        while True:
            nome = input("Digiteum nome: ")
            idade = int(input("Digite uma idade: "))
            email = input("Digite um email: ")

            pessoa = Pessoa(nome=nome, idade=idade, email=email)

            print(pessoa.to_dict())

            return pessoa.to_dict()



    
    def salvar_arquivo(self):
        with open(self.caminho_completo(),"w", encoding="utf-8") as f:
            json.dump(self.dados(), f, indent=4, ensure_ascii=False)
            print(f"Arquivo salvo em: {self.caminho_completo()}")





