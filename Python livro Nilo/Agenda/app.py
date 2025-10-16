from arquivos import SalvarArquivos
from agenda_telefones import Agenda


class Ui(SalvarArquivos, Agenda):
    def __init__(self):
        super().__init__()
        
    def menu(self):
        opcoes = {
            1: self.novo,
            2: self.altera,
            3: self.apaga,
            4: self.lista,
            5: self.grava,
            6: self.le,
            7: self.tamanho_agenda,
        }
        
        return opcoes
    
    def mostrar_menu(self):
        print('''
            1 - Novo
            2 - Altera
            3 - Apaga
            4 - Lista
            5 - Grava
            6 - Lê
            7 - Tamanho
            0 - Sai
        ''')
    
    def validar_entrada_opcoes(self, inicio, fim):
        while True:
            try:
                entrada = int(input("Digite a opcao: "))
                if entrada >= inicio and entrada <= fim:
                    return entrada
            except ValueError as v:
                print(f"Erro: {v}")    
        
    def main(self):
        self.mostrar_menu()
        executar = self.menu()
        
        while True:
            try:
                opcao = self.validar_entrada_opcoes(0, 7)
                
                if opcao == 0:
                    print("Saindo do sistema")
                    break
                
            
                acao = executar.get(opcao)
                
                if acao:
                    acao()
                else:
                    print("Ação invalida")    
            except Exception as e:
                print(f"Erro: {e}")    
                
            
if __name__ == "__main__":
    interface = Ui()
    interface.main()            