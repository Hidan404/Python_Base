from pprint import pprint

def armazenar_produtos() -> list[tuple]:
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

def tuplas_para_dict(tuplas: list[tuple]) -> dict:
    dicionario = {}
    for c, k in tuplas:
        dicionario[c] = k
    return dicionario    

def main():
    produtos = armazenar_produtos()
    dicionario_produtos = tuplas_para_dict(produtos)
    print("Dicionário de produtos:")
    pprint(dicionario_produtos)
    print(f"\nLista de Tuplas: {produtos}")
    
main()    

