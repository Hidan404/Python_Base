import os

def arquivo_quartos():
    return os.path.join(os.path.dirname(__file__), 'quartos.txt')

def reservas():
    return os.path.join(os.path.dirname(__file__), 'reservas.txt')    

def reserva_quarto():
    while True:
        # Mostrar quartos disponíveis
        print("\nQuartos disponíveis:")
        with open(arquivo_quartos(), 'r') as file:
            for line in file:
                print(line.strip())  

        try:
            nome = input("\nDigite seu nome: ").strip()
            numero_quarto = int(input("Digite o número do quarto que deseja reservar: ").strip())
            dias_reservados = int(input("Digite a quantidade de dias que deseja reservar: ").strip())

            # Lê os quartos e prepara atualização
            linhas_modificadas = []
            quarto_encontrado = False
            with open(arquivo_quartos(), 'r') as file:
                for line in file:
                    dados = line.strip().split(',')
                    if dados[0] == str(numero_quarto):
                        quarto_encontrado = True
                        nome_quarto = dados[1].strip()
                        preco = int(dados[2].strip())

                        # Calcula total
                        total = preco * dias_reservados
                        print(f"\nReserva realizada com sucesso! {nome}, você reservou o {nome_quarto} por {dias_reservados} dias. Total a pagar: R$ {total}.")
                        
                        # Marca quarto como ocupado
                        linhas_modificadas.append(f"{numero_quarto}, {nome_quarto}, {preco}, Ocupado\n")
                    else:
                        linhas_modificadas.append(line)

            if not quarto_encontrado:
                print("❌ Quarto não encontrado!")
                continue

            # Atualiza arquivo de quartos
            with open(arquivo_quartos(), 'w') as file:
                file.writelines(linhas_modificadas)

            # Salva reserva no arquivo (sem repetir cabeçalho)
            if not os.path.exists(reservas()):
                with open(reservas(), 'w') as file:
                    file.write("# cliente, quarto, dias\n")
            with open(reservas(), 'a') as file:
                file.write(f"{nome}, {numero_quarto}, {dias_reservados}\n")

            escolha = input("\nDeseja fazer outra reserva? (s/n): ").strip().lower()
            if escolha != 's':
                print("Obrigado por usar nosso sistema de reservas!")
                break         

        except Exception as e:
            print(f"Erro: {e}")
            continue      

if __name__ == "__main__":
    reserva_quarto()
