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
        # Cria cópia para não alterar a lista original
        lista_temporaria = self.lista_alunos.copy()

        aula_ingles = []
        aula_danca = []
        permitidos = 5
        todos_alunos = []

        # Junta todos os alunos em uma lista única
        for alunos in lista_temporaria.values():
            todos_alunos.extend(alunos)

        # Seleciona alunos aleatórios sem repetição
        selecionados = self.selecionados(todos_alunos, permitidos)
        random.seed

        # Adiciona os selecionados na aula e remove da lista_temporaria
        ingles = self.adicionar_alunos(selecionados,aula_ingles,lista_temporaria)
        danca = self.adicionar_alunos(selecionados,aula_danca,lista_temporaria)
        
        print("Alunos na aula de Inglês:", ingles)
        print("Alunos na aula de Inglês:",danca )
        print("Lista temporária após remoção:")
        print(lista_temporaria)

    def selecionados(self, todos, permit):
        return random.sample(todos, permit)

    def adicionar_alunos(self, selecionados, aula, lista_temp):
        # Adiciona os selecionados na aula e remove da lista_temporaria
        for aluno in selecionados:
            aula.append(aluno)
            for sala in lista_temp:
                if aluno in lista_temp[sala]:
                    lista_temp[sala].remove(aluno)
                    
        return aula            

        
# Exemplo de uso:
turma = Alunos()
turma.atividade()

        
      