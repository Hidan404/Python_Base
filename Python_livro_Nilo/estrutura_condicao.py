from pathlib import Path
import json

def coletar_dados(nome: str, email: str, idade: int):
    return {
        "nome": nome,
        "email": email,
        "idade": idade
    }

def caminho():
    return Path(__file__).parent.resolve() / "dados.json"    

def converter_json(*args):
    pessoa = coletar_dados(*args)
    caminho_arquivo = caminho()

    if caminho_arquivo.exists() and caminho_arquivo.stat().st_size > 0: 
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Erro: {e}")    
    else:
        dados = []        

    dados.append(pessoa)   

    with open(caminho_arquivo, "w") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4) 

def ler_arquivo():
    with open(caminho(), "r") as f:
        dados = json.load(f)    
        for d in dados:
            print(d) 


def menu():
    print("""
        Adicioando Pessoas\n
        1 - Adicionar
        2 - Ler arquivo
    """)

def ui():
    while True:
        menu()
        opcao_menu = int(input("Digite uma opcao [1, 2]: "))    

        match(opcao_menu):
            case 1:
                nome = input("Digite nome: ")
                email = input("Digite email: ").strip()
                idade = int(input("Digite sua idade: "))
                if not isinstance(idade, int):
                    print("Digite um numero valido")
                    return
                converter_json(nome, email, idade)  
            case 2:
                ler_arquivo()      

        escolha = input("Digite para continuar S/N").upper()
        if escolha == "S":
            continue
        else:
            break


if __name__ == "__main__":
    ui()



