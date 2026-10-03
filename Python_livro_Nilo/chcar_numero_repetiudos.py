
lista_aleatoria = [47, 22, 26, 17, 20, 9, 24, 38, 48, 23, 20, 21, 49, 38, 15, 49, 10, 14, 41, 16, 49, 36, 49, 11, 26, 6,8, 11, 33, 43, 20, 48, 42, 16, 11, 47, 1, 1, 22, 28, 49, 44, 33, 9, 50, 32, 44, 22, 50, 50, 30, 2, 41,25, 46, 22, 30, 23, 17, 19, 47, 2, 44, 6, 12, 23, 15, 7, 7, 20, 35, 15, 34, 21, 5, 34, 45, 45, 40, 6, 27, 14, 31, 34, 14, 50, 5, 14, 5, 21, 32, 28, 41, 2, 7, 17, 43, 20, 29, 7]
print(lista_aleatoria)

def encontar_primeiro_duplicado(lista):
    numeros_checados = set()
    primeiro_duplicado = 1

    for n in lista:
        if n in numeros_checados:
            primeiro_duplicado = n
            break
        numeros_checados.add(n)

    return primeiro_duplicado    

print(encontar_primeiro_duplicado(lista_aleatoria))