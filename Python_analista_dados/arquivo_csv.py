from pathlib import Path
from tabulate import tabulate

class ArquivoCSV:
    def __init__(self,arquivo: Path):
        self.arquivo = arquivo
        self.conteudo = self.carregar_conteudo(self.arquivo)
        
        

    def carregar_conteudo(self,arquivo) -> list:
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                conteudo = f.readlines()
            return conteudo   
        except Exception as e:
            print(f"Erro: conteudo {e}")  
            return []   
    
    def exibir_tabela(self):
        if not self.conteudo:
            print("⚠️ Nenhum dado para exibir")
            return
        
        cabecalho = self.conteudo[0].strip().split(",")
        dados = [linha.strip().split(",") for linha in self.conteudo[1:] if linha.strip()]
        
        print("\n📊 DADOS DO ARQUIVO CSV")
        print(tabulate(dados, headers=cabecalho, tablefmt="fancy_grid"))

    def extrair_colunas(self, indice):
        coluna = []
        for linha in self.conteudo[1:]:
            conteudo_linha = linha.strip().split(",")
            
            if len(conteudo_linha) > indice:
                coluna.append(conteudo_linha[indice])
        return coluna    

def UI():
    caminho = Path(__file__).parent.resolve() / "emprestimos.csv"
    csv_ = ArquivoCSV(caminho)
    print("####Gerenciamneto do arquivo CSV####")
    while True:
        menu = ["Sair","Exibir","Extrair coluna"]
        opcao = int(input(f"Digite 0 -{menu[0]}\n1 - {menu[1]}\n2 - {menu[2]}: "))
        if opcao == 0:
            break
        elif opcao == 1:
            csv_.exibir_tabela()
        elif opcao == 2:
            indice = int(input("Digite indice: "))
            print(tabulate(csv_.extrair_colunas(indice), tablefmt="ancy_grid"))


if __name__ == "__main__":
    UI()



