import os      # Importa o módulo os que fornece funções para interagir com o sistema operacional
import sys     # Importa o módulo sys que fornece acesso a algumas variáveis e funções do interpretador

# os.walk() gera uma sequência de tuplas, onde cada tupla tem 3 elementos:
# - raiz: caminho atual sendo percorrido
# - diretorios: lista de subdiretórios no caminho atual
# - arquivos: lista de arquivos no caminho atual
# sys.argv[1] é o primeiro argumento passado na linha de comando (caminho inicial)
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print(f"\nCaminho: {raiz}")  # Imprime o caminho atual
    
    # Percorre e imprime todos os subdiretórios do caminho atual
    for d in diretorios:
        print(f"  Diretório: {d}")
    
    # Percorre e imprime todos os arquivos do caminho atual
    for a in arquivos:
        print(f"  Arquivo: {a}")
    
    # Imprime um resumo com a quantidade de diretórios e arquivos encontrados
    print(f"{len(diretorios)} diretórios, {len(arquivos)} arquivos encontrados.")    