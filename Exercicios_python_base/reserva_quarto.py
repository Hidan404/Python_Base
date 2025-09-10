import os

def arquivo_quartos():
    PATH = os.path.join(os.path.dirname(__file__), 'quartos.txt')
    return PATH
def reservas():
    PATH = os.path.join(os.path.dirname(__file__), 'reservas.txt')
    return PATH    

def reserva_quarto():
    with open(arquivo_quartos(), 'r') as file:
        for line in file:
            print(line.strip())  


    while True:
        try:
            nome = input("Digite seu nome: ").strip()
            numero_quarto = int(input("Digite o número do quarto que deseja reservar: ").strip())
            dias_reservados = int(input("Digite a quantidade de dias que deseja reservar: ").strip())
            with open(reservas(), 'a') as file:
                file.write("# cliente, quarto, dias\n")
                file.write(f"{nome}, {numero_quarto}, {dias_reservados}\n")

            linha_modificadas = []
            with open(arquivo_quartos(), 'r') as file:
                for line in file:
                    if line.startswith(str(numero_quarto)):
                        _, nome_quarto, preco = line.strip().split(',')
                        total = int(preco) * dias_reservados
                        print(f"Reserva realizada com sucesso! {nome}, você reservou o {nome_quarto} por {dias_reservados} dias. Total a pagar: R$ {total}.")
                        linha = "Ocupado" + line[1:]
                        linha_modificadas.append(linha)
                    
                        break
            with open(arquivo_quartos(), 'a') as file:
                for linha in linha_modificadas:
                    file.write(linha)
          
        except Exception as e:
            print(f"Erro: {e}")
            continue      



if __name__ == "__main__":
    reserva_quarto()           