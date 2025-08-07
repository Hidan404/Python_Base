import random

__version__ = "0.1.0"

class Alunos:
    def __init__(self):
        self.lista_alunos = {
            "sala1": ["Lucas", "Mateus", "Rafael", "Bruno", "Henrique"],
            "sala2": ["Alex", "Gabriel", "Jordan", "Renan", "Sam"],
            "sala3": ["Zelthor", "Mirelia", "Thandor", "Elwyn", "Kharos"]
        }

    def atividade(self):
        lista_temporaria = self.lista_alunos.copy()

        aula_ingles = []
        aula_danca = []
        aula_fisica = []
        permitidos_por_aula = 5
        todos_alunos = []

        for alunos in lista_temporaria.values():
            todos_alunos.extend(alunos)

        
        selecionados_ingles = self.selecionados(todos_alunos, permitidos_por_aula)
        restantes = [aluno for aluno in todos_alunos if aluno not in selecionados_ingles]
        selecionados_danca = self.selecionados(restantes, permitidos_por_aula)
        restantes = [aluno for aluno in todos_alunos if aluno not in selecionados_ingles and aluno not in selecionados_danca]
        selecionados_fisica = self.selecionados(restantes,permitidos_por_aula)
        

        ingles = self.adicionar_alunos(selecionados_ingles, aula_ingles, lista_temporaria)
        danca = self.adicionar_alunos(selecionados_danca, aula_danca, lista_temporaria)
        fisica = self.adicionar_alunos(selecionados_fisica, aula_fisica,lista_temporaria)

        print("Alunos na aula de Inglês:", ingles)
        print("Alunos na aula de Dança:", danca)
        print("Alunos na aula de Dança:", fisica)

        print("Lista temporária após remoção:")
        print(lista_temporaria)

    def selecionados(self, todos, quantidade):
        return random.sample(todos, quantidade)

    def adicionar_alunos(self, selecionados, aula, lista_temp):
        for aluno in selecionados:
            aula.append(aluno)
            for sala in lista_temp:
                if aluno in lista_temp[sala]:
                    lista_temp[sala].remove(aluno)
        return aula

turma = Alunos()
turma.atividade()


        
      