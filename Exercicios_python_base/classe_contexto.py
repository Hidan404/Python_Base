from pathlib import Path


class Arquivo_criar:
    def __init__(self, nome_arquivo, modo='w'):
        self.nome_arquivo = Path(__file__).parent / nome_arquivo
        self.modo = modo

    def __enter__(self):
        self.arquivo = open(self.nome_arquivo, self.modo)
        return self.arquivo
        
    def __exit__(self, Exception, FileNotFoundError, traceback):
        try:

            self.arquivo.close()
            raise Exception(FileNotFoundError(f"Arquivo '{self.nome_arquivo}' não encontrado."))
        except (Exception, FileNotFoundError) as e:
            print(f"Erro ao fechar o arquivo: {e}")
        except ValueError as e:
            print(f"Valor inválido: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")    


if __name__ == '__main__':
    nome = input("Digite o nome do arquivo: ")
    modo = input("Digite o modo de abertura do arquivo (w para escrita, r para leitura): ")
    with Arquivo_criar(nome, modo) as arquivo:
        arquivo.write('Olá, mundo!')           