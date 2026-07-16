from google import genai
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

def salvar_resposta(msg):
    caminho = Path(__file__).parent.resolve() / "resposta_chatbot.txt"
    with open(caminho, "a", encoding="utf-8") as arquivo:
        arquivo.write(msg)

def chatbot():
    modelo = "gemini-3.1-flash-lite"
    cliente = genai.Client(api_key=os.getenv("CHAVE_APY"))
    while True:
        pergunta = input("Digite sua pergunta: ")
        
        resposta = cliente.models.generate_content_stream(
            model=modelo,
            contents=pergunta,
        )
        resposta_completa = ""
        for chunk in resposta:
            texto = chunk.text
            print(chunk.text, end="", flush=True)
            resposta_completa+= texto
        print()

        salvar_resposta(resposta_completa)

        opcao = input("Deseja continuar S/N: ").upper()
        if opcao == "N":
            print("Saindo...")
            break

      

if __name__ == "__main__":
    chatbot()