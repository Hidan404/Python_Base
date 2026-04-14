from cliente import Cliente



class Banco:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente: Cliente):
        for c in self.clientes:
            if c.nome == cliente.nome:
                raise ValueError("Não adicione o mesmo cliente ja esta cadastrado")
        self.clientes.append(cliente)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nIdade: {cliente.idade}")    
            
    def buscar_cliente(self, nome):
        
        for cliente in self.clientes:
            if nome == cliente.nome:
                return cliente
            
        return 
    
    def conta_cliente_adicioanar(self,nome, conta):
        cliente = self.buscar_cliente(nome)

        if cliente is not None:
            cliente.adicionar_conta(conta)
        else:
            raise ValueError("Erro: Não encontrou")    
        
    def listar_contas(self, nome):
        cliente = self.buscar_cliente(nome)

        if cliente is not None:
            cliente.listar_contas()
        else:
            raise ValueError("Erro: não encontrou conta")   
        
         


                
            