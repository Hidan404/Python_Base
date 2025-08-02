from random import Random


class Item():
    def __init__(self, nome, tipo, poder, qtd):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder
        self.quantidade = qtd
        
    
    def __str__(self):
        return f"{self.nome} | {self.tipo} | {self.poder} | {self.quantidade}"    




class Inventario:
    def __init__(self):
        self.itens = [
            Item("Espada de Fogo", "arma", 50, 2),
            Item("Poção de Vida", "poção", 30, 1),
            Item("Escudo de Ferro", "armadura", 40, 3),
            Item("Arco Elétrico", "arma", 45, 1),
            Item("Poção de Mana", "poção", 25, 5)
        ]

    def listar_itens(self):
        print("\n🎒 Itens disponíveis no inventário:")
        for i, item in enumerate(self.itens, 1):
            print(f"{i}. {item}")

    def obter_item_por_indice(self, indice):
        if 0 <= indice < len(self.itens):
            return self.itens[indice]
        else:
            print("❌ Índice inválido.")
            return None