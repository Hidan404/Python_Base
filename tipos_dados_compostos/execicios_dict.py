def armazenar_produtos() -> list:
    lista_tuplas = []
    while True:
        produto = input("Digite um produto (ou 'sair' para finalizar): ")
        if produto.lower() == 'sair':
            break
        try:
            preco = float(input("Digite um preço: "))
            lista_tuplas.append((produto, preco))
        except ValueError:
            print("Preço inválido. Tente novamente.")
    return lista_tuplas

def tuplas_para_dict(tupla: tuple) -> dict:
    dicioanrio = {}
    for c, k in tupla:
        dicioanrio[c] = k

    return dicioanrio    

def main():
    produtos = armazenar_produtos()
    dicionario_produtos = tuplas_para_dict(produtos)
    print("Dicionário de produtos:", dicionario_produtos)
    print(f"\nLista de Tuplas: {produtos}")
    

main()    

