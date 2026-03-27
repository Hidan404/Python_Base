from contextlib import contextmanager
from pathlib import Path


@contextmanager
def my_open(nome_arquivo, modo='w'):
    try:
        arquivo = open(Path(__file__).parent / nome_arquivo, modo)
        yield arquivo
    except FileNotFoundError as e:
        print(f"Arquivo '{nome_arquivo}' não encontrado: {e}")
    except ValueError as e:
        print(f"Valor inválido: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        arquivo.close()



if __name__ == '__main__':
    nome = input("Digite o nome do arquivo: ")
    modo = input("Digite o modo de abertura do arquivo (w para escrita, r para leitura): ")
    with my_open(nome, modo) as arquivo:
        arquivo.write('Olá, mundo!')