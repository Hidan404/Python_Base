cliente =  {"nome": "Ronald"}
produto = {
    "produto": "Caneta",
    "preco": 5.20
}

coompra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 5
}



total = coompra["quantidade"] * produto["preco"]

print(f"Cliente: {coompra['cliente']['nome']}")
print(f"Produto: {coompra['produto']['produto']}")
print(f"Quantidade: {coompra['quantidade']}")
print(f"Total: {total}")
