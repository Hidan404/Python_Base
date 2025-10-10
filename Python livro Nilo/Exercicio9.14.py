import os
import sys

def entrada_arquivo(nome):
    caminho = os.path.join(os.path.dirname(__file__), nome)
    return caminho

def main():
    # Mostra os arquivos no diretório atual
    #print("Arquivos disponíveis:", os.listdir())

    # Verifica se a quantidade de argumentos está correta
    if len(sys.argv) != 4:
        print("Uso correto: python script.py <arquivo> <linha_inicial> <linha_final>")
        sys.exit(1)

    nome_arquivo = sys.argv[1]
    linha_inicial = int(sys.argv[2])
    linha_final = int(sys.argv[3])
    print(nome_arquivo, linha_inicial, linha_final)

    try:
        with open(entrada_arquivo(nome_arquivo), "r") as f:
            linhas = f.readlines()
            for i, linha in enumerate(linhas, start=1):
                if linha_inicial <= i <= linha_final:
                    print(f"{i}: {linha.strip()}")
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
    except ValueError:
        print("Erro: as linhas inicial e final devem ser números inteiros.")

if __name__ == "__main__":
    main()

            
          