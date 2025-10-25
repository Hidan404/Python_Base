import os
import json

class AcademiaEntrar():
    def __init__(self):
        
        
        self.IDADE_FIXA = 18 
        self.ALTURA_FIXA = 1.70
        self.PESO_FIXO = 60
        self.ARQUIVO = self.salvar_arquivo()
        
    def salvar_arquivo(self):
        path = os.path.join(os.path.dirname(__file__),"academia.json")
        return path
    
    def salvar_dados(self, dados):
        with open(self.ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            
    def carregar_dados(self):
        if not os.path.exists(self.ARQUIVO):
            return []
        try:
            with open(self.ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []    
         
    def main(self):
        caminho_arquivo = self.salvar_arquivo()
        print("""
            Verificar entrada na academia
        """)
        
        while True:
            try:
                escolha = input("Desaja adicionar dados? s/n: ").lower().strip()
                
                if escolha == "s":
                    nome = input("Digite seu nome: ")
                    idade = int(input("Digite sua idade: "))
                    altura = float(input("Digite sua altura: "))
                    peso = float(input("Digite seu peso: "))
                
                    usuarios = self.carregar_dados()
                    usuarios.append({"Nome": nome,"Idade": idade, "Altura": altura, "Peso": peso})
                    
                    self.salvar_dados(usuarios)
                else:
                    print("Opção inválida, digite apenas 's' ou 'n'.")
                    break
                    
            except Exception as e:
                print(f"Erro: {e}")        
                
            
                    
                    
if __name__ == "__main__":
    academia = AcademiaEntrar()
    academia.main()                    
                
                
            
            
            
            
