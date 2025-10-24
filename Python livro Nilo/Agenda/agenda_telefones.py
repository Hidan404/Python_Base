class Agenda():
    def __init__(self):
        self.agenda = []
        
    def pede_nome(self, nome_param="Fulano"):
        try:
            nome = input("Nome: ")
            if len(nome) == 0:
                return nome_param
            return nome
        except ValueError as v:
            print(f"Digite somente numeros {v}")
            
    def email(self):
        email = input("Digite seu email:")
        return email
    
    def aniversario(self):
        aniversario = input("Digite sua data de aniversario: ")
        return aniversario
    
    def pede_telefone(self):
        telefones = []
        while True:
            tipo = input("\nTipo de telefone (Celular/Fixo/Trabalho ou Enter para terminar): ").strip().capitalize()
            if tipo == "":
                break
            numero = input(f"{tipo}: ").strip()
            if numero == "":
                numero = "Não informado"
            elif not numero.isdigit():
                print("Digite somente números!")
                continue
            aniver = self.aniversario()
            email = self.email()
            telefones.append((tipo, numero, aniver, email))
        return telefones
    
    def pede_celular(self):
        return self.pede_telefone("Celular", "Sem celular")

    def pede_trabalho(self):
        return self.pede_telefone("Telefone do Trabalho", "Sem trabalho")

    def pede_fixo(self):
        return self.pede_telefone("Telefone Fixo", "Sem fixo")
    
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
    
    def nome_repetido(self):
        nome = self.pede_nome()
        
    def novo(self):
        nome = self.pede_nome()
        telefone = self.pede_telefone()
        
        if self.pesquisa(nome) is not None:
            print("Nome ja consta na lista")
            return
        
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
    
            
             