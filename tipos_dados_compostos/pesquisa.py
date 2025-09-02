lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pesquisa = int(input("Digite um número para pesquisar: "))
pesquisa2 = int(input("Digite outro número para pesquisar: "))

x = 0
achou1 = False
achou2 = False


while len(lista) > x:
    if lista[x] == pesquisa:
        print(f'Encontrei o número {pesquisa} na posição {x}')
        achou1 = True
    if lista[x] == pesquisa2:
        print(f'Encontrei o número {pesquisa2} na posição {x}')
        achou2 = True
    x += 1
    
if not achou1:
    print(f'Número {pesquisa} não encontrado!')
if not achou2:
    print(f'Número {pesquisa2} não encontrado!')       