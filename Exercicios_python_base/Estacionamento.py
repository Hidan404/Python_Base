from typing import Optional

class Estacionamento:
    def __init__(self):
        # Criamos as listas de objetos "Vaga"
        self.vagas_motos = [Vaga("moto") for _ in range(5)]
        self.vagas_carros = [Vaga("carro") for _ in range(5)]
        
    def estacionar_carro(self, veiculo):
        lista_vagas = self.vagas_carros if isinstance(veiculo, Carro) else self.vagas_motos
        # Procura a primeira vaga de carro que esteja livre
        for vaga in self.vagas_carros:
            if vaga.livre:
                vaga.ocupar(veiculo)
                print(f"Carro {veiculo} estacionado na vaga {vaga.id}")
                return
        print("Erro: Não há vagas de carro disponíveis")

    def remover_carro(self, placa):
        
        for vaga in self.vagas_carros:
            if vaga.placa == placa:
                vaga.livre = True
                vaga.placa = None
                print(f"Carro {placa} saiu da vaga {vaga.id}")
                return
        print(f"Erro: Veículo {placa} não encontrado")

    def estado_estacionamento(self):
        livres_moto = sum(1 for v in self.vagas_motos if v.livre)
        livres_carro = sum(1 for v in self.vagas_carros if v.livre)
        
        print(f"\n--- Status ---")
        print(f"Motos: {livres_moto} livres / {len(self.vagas_motos)} total")
        print(f"Carros: {livres_carro} livres / {len(self.vagas_carros)} total")



class Vaga:
    _contador = 1
    def __init__(self, tipo: str):
        self.id = Vaga._contador
        self.tipo = self.verificar(tipo)
        self.livre = True
        self.placa = None

        Vaga._contador+= 1

    def verificar(self, tipo):
        if tipo not in ["carro", "moto"]:
            raise ValueError(f"Erro; Tipo tem que ser Moto ou Carro")
        return tipo


    def ocupar(self, placa):
        if not self.livre:
            raise ValueError(f"Erro: Vaga {self.id} já está ocupada")
        
        self.livre = False
        self.placa = placa
        print(f"Vaga {self.id} ocupada pelo veículo {placa}")
        
        

    def desocupar(self, placa):
        if self.livre:
            raise ValueError(f"Erro: Vaga {self.id} já está livre")
        
        self.livre = True
        self.placa = placa
        print(f"Vaga {self.id} ocupada pelo veículo {placa}")

class Carro():
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        if not self.estacionado:
            self.estacionado = True
        return self.estacionado    

    def sair_da_vaga(self):
        if self.estacionado:
            self.estacionado = False
        return self.estacionado    


class Moto():
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False

    def estacionar(self):
        if not self.estacionado:
            self.estacionado = True
        return self.estacionado    

    def sair_da_vaga(self):
        if self.estacionado:
            self.estacionado = False
        return self.estacionado 




if __name__ == "__main__":
    