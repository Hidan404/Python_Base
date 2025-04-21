listas_animes = ['Attack on Titan', 'Death Note', 'Naruto', 'One Piece', 'My Hero Academia']

def adicioanr_anime():
    while True:
        add_anime = input('Digite o nome do anime que deseja adicionar: ')
        if add_anime == "":
            break

        listas_animes.append(add_anime)
        print(f"Anime {add_anime} adicionado com sucesso!")

        return listas_animes
adicioanr_anime()

def insert_anime():
    while True:
        insert_anime = input('Digite o nome do anime que deseja adicionar: ')
        if insert_anime == "":
            break

        listas_animes.insert(0, insert_anime)
        print(f"Anime {insert_anime} adicionado com sucesso!")

        return listas_animes
insert_anime()

def remover_anime(indice):
    if indice < 0 or indice >= len(listas_animes):
        print("Índice inválido.")

    listas_animes.pop(indice)    

    return listas_animes
remover_anime(2)  # Remove o anime na posição 2 (terceiro anime)

def remover_anime_nome(nome):
    if nome in listas_animes:
        listas_animes.remove(nome)
        print(f"Anime {nome} removido com sucesso!")
    else:
        print(f"Anime {nome} não encontrado na lista.")

    return listas_animes
remover_anime_nome("Naruto")  # Remove o anime "Naruto"

lista_animes_atuais = [a if a != "" else f"{a}\n" for a in listas_animes]  # Remove animes vazios
print("\nLista de animes atuais:")
print(lista_animes_atuais)