import json
from pathlib import Path

class GerenciadorNotas:
    def __init__(self, nome_arquivo="notas.json"):
        self.nome_arquivo = nome_arquivo
        self.caminho_arquivo = Path(__file__).resolve().parent / self.nome_arquivo

    def carregar_dados(self):
        """Carrega os dados existentes do JSON. Cria o arquivo se não existir."""
        if not self.caminho_arquivo.exists():
            return {} # Retorna um dicionário vazio se o arquivo for novo
        
        with self.caminho_arquivo.open("r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                # Caso o arquivo exista mas esteja vazio/corrompido
                return {}

    def salvar_dados(self, dados):
        """Salva todos os dados de volta no arquivo JSON."""
        with self.caminho_arquivo.open("w", encoding="utf-8") as arquivo:
            # indent=4 deixa o JSON formatado e fácil de ler
            json.dump(dados, arquivo, indent=4)

    def adicionar_notas(self, nome_aluno, notas_novas):
        """Adiciona notas a um aluno específico."""
        # 1. Carrega o estado atual de todos os alunos
        dados_alunos = self.carregar_dados()
        
        # 2. Verifica se o aluno já existe nos dados carregados
        if nome_aluno not in dados_alunos:
            dados_alunos[nome_aluno] = [] # Cria uma lista vazia para o novo aluno
            
        # 3. Adiciona as novas notas à lista existente
        dados_alunos[nome_aluno].extend(notas_novas)
        
        # 4. Salva o dicionário completo de volta no arquivo JSON
        self.salvar_dados(dados_alunos)
        print(f"Notas adicionadas para {nome_aluno}.")

    def main(self):
        """Loop principal para interação com o usuário."""
        nome_entrada = input("Digite o nome do Aluno: ")
        notas_a_adicionar = []

        print(f"Adicionando notas para {nome_entrada}. Digite 4 notas:")

        for i in range(4):
            while True:
                try:
                    # Usamos f-string para indicar qual nota estamos pedindo (1, 2, 3 ou 4)
                    nota = float(input(f"Digite a {i+1}ª nota: "))
                    notas_a_adicionar.append(nota)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        
        self.adicionar_notas(nome_entrada, notas_a_adicionar)
        print("Processo concluído.")

# Exemplo de uso:
if __name__ == "__main__":
    gerenciador = GerenciadorNotas()
    gerenciador.main()



    
