from pathlib import Path

# Obtém o caminho do diretório onde o script está sendo executado
script_dir = Path(__file__).resolve().parent

try:
    # Define o caminho para a nova pasta dentro do diretório do script
    criar_pasta = script_dir / "nova_pasta_exemplo"
    criar_pasta.mkdir(exist_ok=True)
    print("Pasta criada em:", criar_pasta)

except PermissionError:
    # Isso só acontecerá se o próprio diretório do script for de somente leitura
    print(f"Erro de permissão: Não foi possível criar o diretório em {criar_pasta}.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
