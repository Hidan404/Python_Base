sala1 = ["erik", "ana", "joão", "maria", "paulo", "lucas"]
sala2 = ["carla", "bruno", "fernanda", "juliana", "roberto", "camila"]


aula_ingles = sala1[:2] + sala2[:2]
aula_musica = sala1[2:] + sala2[2:]
lista_zip = [(x, y) for x, y in zip(sala1, sala2)]
aula_danca = [i for par in lista_zip for i in par]


atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca)
]

for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade {nome_atividade}")
    print("_" * 40)

    atividade_sala1 = set(sala1).intersection(atividade)
    atividade_sala2 = set(sala2).intersection(atividade)

    print("sala1", atividade_sala1)
    print("sala2", atividade_sala2)

    print()
    print("#" * 40)