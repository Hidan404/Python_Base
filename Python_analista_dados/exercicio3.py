produtos = {
    "bolo": 20.0,
    "torta": 25.0,
    "sorvete": 15.0
}

sabores = {
    "chocolate": 2.0,
    "morango": 1.5,
    "baunilha": 1.0
}


coberturas = {
    "granulado": 1.0,
    "calda": 1.5,
    "castanha": 2.0
}

pedidos_realizados = []

def menu():
    print("\nSorveteria Doce Sabor")
    print("1. Ver cardápio")
    print("2. Fazer pedido")
    print("3. Valor a ser pago (total de todos os pedidos)")
    print("4. Sair")
    try:
        escolha = int(input("Escolha uma opção: "))
        return escolha
    except ValueError:
        print("Digite um número válido.")
        return 0

def ver_cardapio():
    print("\n--- Produtos ---")
    for item, valor in produtos.items():
        print(f"{item.capitalize()} = R$ {valor:.2f}")
    print("\n--- Sabores (acréscimo) ---")
    for item, valor in sabores.items():
        print(f"{item.capitalize()} = R$ {valor:.2f}")
    print("\n--- Coberturas (acréscimo) ---")
    for item, valor in coberturas.items():
        print(f"{item.capitalize()} = R$ {valor:.2f}")

def registrar_escolha(catalogo, escolha_usuario):

    escolha_normalizada = escolha_usuario.strip().lower()
    if escolha_normalizada in catalogo:
        return {escolha_normalizada: catalogo[escolha_normalizada]}
    else:
        print(f"Opção '{escolha_usuario}' não encontrada.")
        return None

def fazer_pedido():
  
    print("\n--- Novo Pedido ---")
    
   
    produto_nome = input("Digite o nome do produto: ")
    produto_escolhido = registrar_escolha(produtos, produto_nome)
    if produto_escolhido is None:
        return 0  
    
    sabor_nome = input("Digite o nome do sabor: ")
    sabor_escolhido = registrar_escolha(sabores, sabor_nome)
    if sabor_escolhido is None:
        sabor_escolhido = {} 

    cobertura_nome = input("Digite o nome da cobertura: ")
    cobertura_escolhida = registrar_escolha(coberturas, cobertura_nome)
    if cobertura_escolhida is None:
        cobertura_escolhida = {}
    

    subtotal = (list(produto_escolhido.values())[0] +
                (list(sabor_escolhido.values())[0] if sabor_escolhido else 0) +
                (list(cobertura_escolhida.values())[0] if cobertura_escolhida else 0))
    

    pedido_atual = {
        "produto": produto_escolhido,
        "sabor": sabor_escolhido,
        "cobertura": cobertura_escolhida,
        "subtotal": subtotal
    }
    pedidos_realizados.append(pedido_atual)
    
    print(f"Pedido adicionado! Subtotal: R$ {subtotal:.2f}")
    return subtotal

def calcular_total_geral():
    if not pedidos_realizados:
        print("Nenhum pedido foi feito ainda.")
        return 0
    total = 0
    print("\n--- Todos os Pedidos ---")
    for i, ped in enumerate(pedidos_realizados, 1):
        prod = list(ped["produto"].keys())[0]
        sabor = list(ped["sabor"].keys())[0] if ped["sabor"] else "nenhum"
        cobertura = list(ped["cobertura"].keys())[0] if ped["cobertura"] else "nenhuma"
        print(f"{i}. Produto: {prod} | Sabor: {sabor} | Cobertura: {cobertura} | Subtotal: R$ {ped['subtotal']:.2f}")
        total += ped["subtotal"]
    print(f"Total a pagar: R$ {total:.2f}")
    return total

def main():
    while True:
        opcao = menu()
        if opcao == 1:
            ver_cardapio()
        elif opcao == 2:
            fazer_pedido()
        elif opcao == 3:
            calcular_total_geral()
        elif opcao == 4:
            print("Obrigado pela visita!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()