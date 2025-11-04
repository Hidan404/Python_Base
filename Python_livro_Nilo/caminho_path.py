import os.path

caminho_atual = os.path.dirname(__file__)

print(f"\n{os.path.abspath(caminho_atual)}")
print(f"{os.path.basename(caminho_atual)}")
print(f"{os.path.dirname(caminho_atual)}")
print(f"{os.path.split(caminho_atual)}")
print(f"{os.path.join(caminho_atual, 'subpasta', 'arquivo.txt')}\n")