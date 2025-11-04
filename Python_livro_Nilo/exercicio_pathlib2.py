"""
🔹 Exercício 2 – Listar arquivos .txt

👉 Crie um script que:

Use Path(".") para apontar para a pasta atual.

Liste todos os arquivos .txt existentes.

Mostre o nome de cada arquivo encontrado.

💡 Utilidade real: organizar ou varrer pastas para encontrar anotações, logs ou backups.
"""


from pathlib import Path




def procurar_raiz_do_sistema_operacional():
    pasta_atual = Path(".").absolute()
    raiz = Path(pasta_atual.anchor)
    print(f"Raiz do sistema operacional: {raiz}")
    arquivos_txt = raiz.rglob("*.txt")


    return arquivos_txt

def dir_do_scritp():
    diretorio_atual = Path(__file__).parent.absolute()
    print(f"Diretório atual do script: {diretorio_atual}")
    return diretorio_atual / "arquivos_txt.txt"



def diretorios_salvar_arquivos():
    raiz = procurar_raiz_do_sistema_operacional()
    for a in raiz:
        with open(dir_do_scritp(), "a", encoding="utf-8") as f:
            f.write(f"{a}\n")


if __name__ == "__main__":
    diretorios_salvar_arquivos()
    

