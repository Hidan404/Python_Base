frase = "ACDTTTAPII"
contador = 0
frase_dict = {}

for f in frase:
    if f in frase_dict:
        frase_dict[f] = frase_dict.get(f, 0) + 1
    else:
        frase_dict[f] = 1
print(frase_dict)   