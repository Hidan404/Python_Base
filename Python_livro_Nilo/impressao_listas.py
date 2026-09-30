# Três listas diferentes de produtos com nome, preço e quantidade

'''lista_1 = [
    {"produto": "Maçã", "preco": 2.50, "qtd": 5},
    {"produto": "Banana", "preco": 3.00, "qtd": 7},
    {"produto": "Laranja", "preco": 2.20, "qtd": 4},
]

lista_2 = [
    {"produto": "Leite", "preco": 4.50, "qtd": 3},
    {"produto": "Pão", "preco": 8.00, "qtd": 2},
    {"produto": "Ovo", "preco": 6.50, "qtd": 10},
]

lista_3 = [
    {"produto": "Arroz", "preco": 25.00, "qtd": 2},
    {"produto": "Feijão", "preco": 18.00, "qtd": 3},
    {"produto": "Óleo", "preco": 12.50, "qtd": 4},
]

lista = [lista_1, lista_2, lista_3]

for i in lista:
    for j in i:
        for k ,v in j.items():
            print(f"Chave: {k} | Valor: {v}")


produtos = [produtos for lista_produtos in lista for produtos in lista_produtos]   
for p in produtos:
    print(p)         

'''
compras = []

while True:
    produto = input("nome ou S para sair: ").upper().strip()
    if produto.startswith("S"):
        print("Saindo...")
        break
    qtd = int(input("Digite qtd: "))
    preco = float(input("Digite o preço: "))

    compras.append([produto, qtd, preco])

for p in compras:
    total = p[1] * p[2]
    print(f'''
        produto: {p[0]} | qtd: {p[1]} | preço: {p[2]:.2f} | total: {total:.2f}
    ''') 