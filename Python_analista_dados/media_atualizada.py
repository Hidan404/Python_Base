lista_medias = [8.9,7.5,4.2,1.4,9.5]
lista_media_atualizada = []
nota_a_mais = 1
'''for i in lista_medias:
    if (i + nota_a_mais) > 10:
        lista_media_atualizada.append(10)
    else:
        lista_media_atualizada.append(i + nota_a_mais)
print(lista_media_atualizada)  
'''

lista_media_atualizada = [min(i + nota_a_mais,10) for i in lista_medias]
print(lista_media_atualizada)