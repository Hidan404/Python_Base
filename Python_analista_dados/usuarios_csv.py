from pathlib import Path
import csv



def arquivo():
    return Path(__file__).parent.resolve() / "usuarios.csv"

def ler_arquivo(arquivo_funcao: Path) -> list:
    arquivo = arquivo_funcao()
    lista_ids = []
    
    with open(arquivo, "r", encoding="utf-8" ) as f:
        primeira_linha = f.readlines()[1:]
    
        print(primeira_linha)

        for i in primeira_linha:
            linha_separada = i.split(",")[0]
            id = int(linha_separada)
            lista_ids.append(id)

    return lista_ids      

def escrever_no_arquivo(arquivo_funcao: Path) -> int:
    arquivo = arquivo_funcao()
    def pegar_ultimo_id():
        with open(arquivo, "r", encoding="utf-8") as fp:
            arquivo_id = fp.readlines()[-1].split(",")[0]
            print(arquivo_id)
        return int(arquivo_id) + 1  
    
    ultimo_id = pegar_ultimo_id()

    id = ultimo_id
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    idade = int(input("Idade: "))
    cargo = input("Cargo: ")
    status = input("Status (Ativo/Inativo): ")

    with open(arquivo, "a", encoding="utf-8", newline="") as f:
        arquivo = csv.writer(f)

        arquivo.writerow(
            [id,nome,email,telefone,cidade,estado,idade,cargo,status]
        )

def procurar_por_id(funcao):
    arquivo = funcao()
    try:
        with open(arquivo, "r", encoding="utf-8") as fp:
            linhas = fp.readlines()[1:]
            id_entrada = int(input("Digite um id: "))
            for l in linhas:
                id = int(l.split(",")[0])
                dados = l.split(",")
                if id == id_entrada:
                    resultado =f"Nome: {dados[1]}, Cidade: {dados[4]}" 
                    return resultado
            else:
                return "Id do usuario não encontrado"    
    except Exception as e:
        raise ValueError(f"Erro id fora do alcances {str(e)}")        


def deletar_por_id(funcao):
    arquivo = funcao()
    
    with open(arquivo, "r", encoding="utf-8" ) as f:
        dados = f.readlines()
    if not dados:
        print("arquivo esta vazio ")
        return

    cabecalho = dados[0]
    nova_lista = [cabecalho]

    id_entrada = int(input("Digite seu ID: "))

    for d in dados[1:]:
        id_usuario = int(d.split(",")[0])
        if id_usuario != id_entrada:
            nova_lista.append(d) 
    print(nova_lista)        
          
    with open(arquivo, "w", encoding="utf-8") as fp:
        fp.writelines(nova_lista)
       
        

        
#print(ler_arquivo(arquivo))            
#escrever_no_arquivo(arquivo)s
#print(procurar_por_id(arquivo))
deletar_por_id(arquivo)