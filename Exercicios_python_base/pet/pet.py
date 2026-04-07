class Pet():
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def print_info(self):
        print(f"Nome: {self.name}")
        print(f"Espécie: {self.species}")
        print(f"Idade: {self.age} anos")    


        