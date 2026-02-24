lista = ["01101000", "01100101", "01101100", "01101100", "01101111"]

texto = "".join([chr(int(str(i), 2)) for i in lista])
print(texto)

teste = int("01101000", 2)
teste2 = chr(teste)
print(teste)
print(teste2)