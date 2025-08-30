import itertools

lista1 = [1,8,3]
lista2 = [8,912, 15]
lista3 = [78, 12, 65, 4]

lista_total = list(itertools.zip_longest(lista1, lista2, lista3, fillvalue=None))
lista_sem_tuplas = []
for l in lista_total:
    for li in l:
        lista_sem_tuplas.append(li)

print(lista_sem_tuplas)   


l = list(set(itertools.zip_longest(lista1, lista2)))
l_o = [x for x in l]
print(l_o)



        
