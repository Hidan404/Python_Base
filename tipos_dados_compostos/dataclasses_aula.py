from dataclasses import dataclass

#@dataclass(init=False) tenho que definir meu proprio init da classe
@dataclass()
class Pessoa:
    nome: str
    sobrenome: str
    idade: int

    #def __post_init__():
        #print("Depois do init")


    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
    @nome_completo.setter
    def nome_completo(self,valores):
        nome, *sobrenome = valores.split(" ")
        self.nome = nome
        self.sobrenome = " ".join(sobrenome)




if __name__ == "__main__":
    pessoa1 = Pessoa("Hidan","Jashin", 21)     
    pessoa2 = Pessoa("kakuzu", "tataro",98)
    print(pessoa1 == pessoa2)   
    pessoa1.nome_completo = "Ronald Antonio vaurz"
    print(pessoa1.nome_completo)

    #sorted() ordena a lista de pessoas, para isso tem que ser definido o order = True no dataclass
    lista_pessoas = [Pessoa("Hidan","Jashin", 21), Pessoa("kakuzu", "tataro",98), Pessoa("Itachi","Uchiha", 21)]
    #print(sorted(lista_pessoas))

    print(sorted(lista_pessoas,reverse=True, key=lambda pessoa: pessoa.idade))
