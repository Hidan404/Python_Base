def imprimir_listas(lista,caractere=" ",nivel=2):
    for i in lista:
        if isinstance(i, int):
            print(f"{caractere * nivel}{i}")
        else:
            imprimir_listas(i,nivel+1)  


listas_numeros = [1, [4,5,6], 5, 8,10]    
imprimir_listas(listas_numeros, "*")          