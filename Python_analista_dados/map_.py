# Exemplo original simples
lista = [2,5,7,8,9,6,4,12]

maior_numero = lambda n: n * 2

resultado = list(map(maior_numero, lista))
print(resultado)


# Exemplo do mundo real: aplicação de desconto em uma lista de produtos
# Cada produto é um dicionário com nome e preco
produtos = [
	{"nome": "Camiseta", "preco": 50.0},
	{"nome": "Calça", "preco": 120.0},
	{"nome": "Tenis", "preco": 200.0},
]

def aplica_desconto(percentual):
	"""Função de alta ordem que retorna uma função que aplica um desconto percentual."""
	def desconto(produto):
		novo_preco = round(produto["preco"] * (1 - percentual / 100), 2)
		# retorna novo dicionário para não mutar o original
		return {"nome": produto["nome"], "preco": novo_preco}
	return desconto

# Criamos uma função que aplica 20% de desconto
desconto_20 = aplica_desconto(20)

# Usamos map para aplicar a função de desconto a cada produto
produtos_com_desconto = list(map(desconto_20, produtos))

print(produtos_com_desconto)


