estoque = {
    "001": {"nome": "Caneta", "quantidade": 100, "preco": 1.50},
    "002": {"nome": "Caderno", "quantidade": 200, "preco": 5.00},
    "003": {"nome": "Borracha", "quantidade": 150, "preco": 0.75},
    "004": {"nome": "Lápis", "quantidade": 300, "preco": 0.50},
    "005": {"nome": "Mochila", "quantidade": 50, "preco": 120.00},
}


def exibir_estoque(estoque2):
    print("Estoque Da loja Atual")
    for id, item in estoque2.items():
        nome = item["nome"]
        qtd = item["quantidade"]
        preco = item["preco"]
        print(f"Nome: {nome} | Qtd: {qtd} | Preco: {preco}")

exibir_estoque(estoque)        


def venda():
    quantidade = int(input("Digite a quantidade de items: "))
    produto = input("Digite o produto: ")

    for id, items in estoque.items():
        if produto == items["nome"]:
            