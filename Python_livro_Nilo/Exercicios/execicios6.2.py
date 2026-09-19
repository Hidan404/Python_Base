lista1 = [1,2]
lista2 = [3,4]
lista3 = []

#lista3 = zip(lista1, lista2)
#lista3 = [i for i in lista3]
lista3 = lista1 + lista2

print(lista3)

lista4 = lista3[:2]
print(lista4)
del lista4[1]
print(lista4)