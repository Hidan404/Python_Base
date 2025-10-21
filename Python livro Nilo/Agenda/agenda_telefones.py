class Agenda():
    def __init__(self):
        self.agenda = []
        
    def pede_nome(self, nome_param="Fulano"):
        try:
            nome = int(input("Telefone: "))
            if len(nome) == 0:
                return nome_param
            return nome
        except ValueError as v:
            print(f"Digite somente numeros {v}")
    
    def pede_telefone(self, telefone_param =111):
        try:
            telefone = int(input("Telefone: "))
            if len(telefone) == 0:
                return telefone_param
            return telefone
        except ValueError as v:
            print(f"Digite somente numeros {v}")
    
    def mostra_dados(self,nome, telefone):
        print(f"Nome: {nome} - Telefone: {telefone} ")
        
    def pede_nome_arquivo(self):
        return input("Nome arquivo: ")     
    
    def pesquisa(self,nome):
        mnome = nome.lower()
        for p, e in enumerate(self.agenda):
            if e[0].lower() == mnome:
                return p
            
        return None
    
    def novo(self):
        nome = self.pede_nome()
        telefone = self.pede_telefone()
        
        self.agenda.append([nome, telefone])   
        
    def apaga(self):
        nome = self.pede_nome()
        pesquisa = self.pesquisa(nome)
        
        if pesquisa is not None:
            del self.agenda[pesquisa]
        else:
            print("Contato não esta na agenda")    
            
            
    def altera(self):
        pesquisa = self.pesquisa()
        if pesquisa is not None:
            nome = self.agenda[pesquisa][0]
            telefone = self.agenda[pesquisa][1]
            print("Encontrado")
            self.mostra_dados(nome, telefone)
            
            nome_novo = self.pede_nome()
            telefone_novo = self.pede_telefone()
            
            self.agenda[pesquisa] = [nome_novo, telefone_novo]    
            print(f"Dados laterados {nome}, {telefone} = {self.mostra_dados(nome_novo, telefone_novo)}")    
    
    def lista(self):
        print("====Agenda de Contatos====\n")
        for a in self.agenda:
            self.mostra_dados(a[0], a[1])
        print("\n====Fim=====\n")   
        
    def lista_ordem(self):
        print("====Agenda de Contatos====\n")
        agenda_ordem = sorted(self.agenda, key=lambda contato: contato[0])
        for a in agenda_ordem:
            self.mostra_dados(a[0], a[1])
        print("\n====Fim=====\n")   
    
            
             