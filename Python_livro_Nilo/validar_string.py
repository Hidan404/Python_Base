def validar_string(texto,minimo, maximo):
    comprimento = len(texto)

    if comprimento >= minimo and comprimento <= maximo:
        return True
    else:
        return False

#print(validar_string("Ronald",2, 7))            



def comparar_string_lista(texto, lista):
    for l in lista:
        if texto in l:
            resultado = f"{l}"
            return True, resultado
        
    return False     



print(comparar_string_lista("Ronald",["Hidan", "Sabrina", "Ronald"]))                  