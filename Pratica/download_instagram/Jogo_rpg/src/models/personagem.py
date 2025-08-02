from inventario import Inventario

class Personagem():
    def __init__(self, nome):
        self.nome = nome
        self.HP = 100
        self.nivel = 1
        self.forca = 3
        self.experiencia = 0
        self.inventario = []
        self.status = "vivo"
        
    def atacar(self):
        dano = self.forca
        return dano    
        
    def usar_item(self):
        inventario = Inventario()  
        inventario.listar_itens() 
        
        escolha_item = input("Es")
        
        
p = Personagem("Hidan")
print(p.usar_item())        