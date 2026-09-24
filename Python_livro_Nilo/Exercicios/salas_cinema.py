lista = [10, 2, 1, 3, 0]

while True:
    sala = int(input("Digite uma sala, 0 para sair: "))
    print(lista[sala -1])

    if sala == 0:
        print("saindo...")
        break
    if sala > len(lista) or sala < 1:
        print("sala invalida")
    elif lista[sala -1] == 0:
        print("nao tem vagas")  
    else:
        preencher = int(input(f"Quantos lugares restantes {lista[sala -1]} "))
        if preencher > lista[sala -1]:
            print("Sem vagas disponiveis")
        elif preencher < 0:
            print("Digite um numero valido")
        else:
            lista[sala -1]-= preencher
            print(f"Lugares vendidos {preencher}")

for sala, vaga in enumerate(lista):
    print(f"sala: {sala + 1} | vaga: {vaga}")                    

