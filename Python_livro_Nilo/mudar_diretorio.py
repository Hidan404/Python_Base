import os 
from pathlib import Path

pasta_atual = Path(__file__).resolve().parent
print(f"Pasta do script: {pasta_atual}")

# Mudar para o diretório pai (independente da condição)
os.chdir("../")
print(f"Diretório atual: {Path.cwd()}")


