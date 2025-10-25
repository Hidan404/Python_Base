import sys, os

def root_path(arquivo_nome):
    return os.path.join(os.path.dirname(__file__), arquivo_nome)

def main():
    if len(sys.argv) != 4:
        print("Uso incorreto!")
        print("Exemplo: python script.py arquivo1.txt arquivo2.txt saida.txt")
        return

    entrada1 = root_path(sys.argv[1])
    entrada2 = root_path(sys.argv[2])
    saida = root_path(sys.argv[3])

    # Verifica se os arquivos existem
    if not os.path.exists(entrada1):
        print(f"Arquivo não encontrado: {entrada1}")
        return
    if not os.path.exists(entrada2):
        print(f"Arquivo não encontrado: {entrada2}")
        return

    # Lê os dois arquivos e junta o conteúdo
    with open(entrada1, "r") as f1, open(entrada2, "r") as f2:
        conteudo = f1.readlines() + f2.readlines()

    # Escreve o resultado no arquivo de saída
    with open(saida, "w") as f_saida:
        f_saida.writelines(conteudo)

    print(f"Conteúdo mesclado em: {saida}")

if __name__ == "__main__":
    main()

                
              