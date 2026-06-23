# Exemplo de vida real: filtrar produtos disponíveis que um cliente pode comprar
# com base em seu orçamento e se o produto está em estoque.

produtos = [
    {"nome": "camisa", "preco": 80, "estoque": 10},
    {"nome": "shorts", "preco": 54, "estoque": 0},
    {"nome": "meias", "preco": 12, "estoque": 50},
    {"nome": "jaqueta", "preco": 150, "estoque": 3},
]

# Cenário: um cliente tem um orçamento disponível (por exemplo, R$ 60)
orcamento_cliente = 60

# Função/condição usada pelo filter:
# retorna True se o produto estiver em estoque (estoque > 0)
# e o preço for menor ou igual ao orçamento do cliente.
def pode_comprar(produto):
    return produto.get("estoque", 0) > 0 and produto.get("preco", float("inf")) <= orcamento_cliente

# Aplicando filter para obter apenas os produtos que o cliente pode comprar agora
resultado = list(filter(pode_comprar, produtos))

print(resultado)

# Lista de emails com vários domínios diferentes
emails = [
    "joao@gmail.com",
    "maria@hotmail.com",
    "pedro@outlook.com",
    "ana@yahoo.com",
    "carlos@empresa.com.br",
    "paula@usp.edu.br",
    "lucas@icloud.com",
    "julia@protonmail.com",
    "rafael@microsoft.com",
    "fernanda@facebook.com",
    "ronald@microsoft.com"
]

emails_microsoft = lambda email: "microsoft.com" in email
resultado = filter(emails_microsoft, emails)
print(list(resultado))





