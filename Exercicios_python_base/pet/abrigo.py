from pet import Pet

class Abrigo():
    def __init__(self):
        self.__pets = []

    def adicionar_pet(self, pet):
        self.__pets.append(pet)

    def listar_pets(self):
        for pet in self.__pets:
            pet.print_info()
            print()


if __name__ == '__main__':
    abrigo = Abrigo()

    pet1 = Pet("Rex", "Cachorro", 5)
    pet2 = Pet("Mia", "Gato", 3)

    abrigo.adicionar_pet(pet1)
    abrigo.adicionar_pet(pet2)

    print("Pets no abrigo:\n")
    abrigo.listar_pets()            