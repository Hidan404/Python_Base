letras_numeros = {"a": 1, "b": 2}
dict_o = {chave: valor * 2 for chave, valor in letras_numeros.items() if valor % 2 == 0}
print(dict_o)