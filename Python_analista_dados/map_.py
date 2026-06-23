lista = [2,5,7,8,9,6,4,12]

maior_numero = lambda n: n if n > 9 else False

resultado = list(map(maior_numero, lista))
print(resultado)