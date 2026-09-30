perguntas = [
    {
        "pergunta": "quanto é 5 * 5",
        "opcoes": [1,5,6,25],
        "resposta": 25
    },
    {
        "pergunta": "quanto é 10 + 7",
        "opcoes": [15,17,20,27],
        "resposta": 17
    },
    {
        "pergunta": "quanto é 20 - 8",
        "opcoes": [10,12,14,16],
        "resposta": 12
    },
    {
        "pergunta": "quanto é 6 * 4",
        "opcoes": [18,20,24,28],
        "resposta": 24
    },
    {
        "pergunta": "quanto é 36 / 6",
        "opcoes": [4,5,6,7],
        "resposta": 6
    }
]

def main():
    respostas_certas = 0
    
    print("Show de perguntas")
    for i in perguntas:
        alternativas = 0
        

        print(f"pergunta: {i['pergunta']}")
        for j in i["opcoes"]:
            alternativas += 1
            print(f"{alternativas}) {j}")

        escolha = int(input("Digite sua resposta: "))
        if escolha == j:
            print(f"Esta correto {escolha} == {j}")
            respostas_certas+= 1
        else:
            print(f"Esta incorreto {escolha} != {j}")    

    print(f"Respostas certas {respostas_certas}")        
            

main()