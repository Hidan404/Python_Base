from google import genai
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

cliente = genai.Client(api_key=os.getenv("CHAVE_APY"))
resposta = cliente.models.generate_content_stream(
    model="gemini-3.1-flash-lite",
    contents="me faça um planejamneto para desenvolver uma aplicação gerenciador de senhas com as stacks python streamlit criptografia as senhas devem ser salvas criptografadas em um BD junto com a apliocação gere o planejamento e oprompt  para geracaodo da aplicação em etapas",
)

for chunk in resposta:
    print(chunk.text, end="", flush=True)
print()