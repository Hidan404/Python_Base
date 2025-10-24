def lista_pessoas():
    pessoas = int(input("Quantas pessoas convidadas? "))
    return pessoas

def nome_pessoas(pessoas_quantidade):
    lista_convidados = []
    for pessoas in range(pessoas_quantidade):
        nome = input("Digite o nome: ")
        lista_convidados.append(nome)
    
    return lista_convidados

def imprimir_convidados(convidados):
    print("\nLista de Convidados\n")
    for c in convidados:
        print(f"Convidado: {c}")    
        
def ui():
    lista_people = lista_pessoas()
    
    nome_people = nome_pessoas(lista_people)
    imprimir_convidados(nome_people)

ui()           