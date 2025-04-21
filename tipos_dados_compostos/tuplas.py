lista_akatuski = ("itachi", "deidara", "sasori", "kakuzu", "hidan", "konan", "pain", "zetsu", "obito", "madara")

print(lista_akatuski.count("itachi"))  
print(lista_akatuski.index("itachi"))  

for membro in lista_akatuski:
    print(f"--> {membro.title()}")  # Converte o nome do membro para título


deidara = lista_akatuski[1]
print(f"\nDeidara é o {deidara} da akatuski")  