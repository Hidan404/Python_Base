from pathlib import Path
from openai import OpenAI
import json
import re
import time

caminho = Path(__file__).parent.resolve() / "resenha.txt"

cliente = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    timeout=60.0,  # tempo de espera para saida de resposta
)

def carregar_arquivo(caminho_):
    lista = []
    try:
        with open(caminho_, "r", encoding="utf-8") as f:
            for linha in f:
                lista.append(linha.strip())
    except UnicodeDecodeError:
        with open(caminho_, "r", encoding="latin-1") as f:
            for linha in f:
                lista.append(linha.strip())
    return lista

def ia_lmstudio(pergunta):
    resposta = cliente.chat.completions.create(
        model="google/gemma-3-1B",  # trocar modelo para determinado proposito
        messages=[
            {
                "role": "system",
                "content": (
                    "Receba uma linha no formato id$usuario$resenha. "
                    "Retorne APENAS JSON puro com as chaves id, usuario, resenha. "
                    "NÃO use formatação, nem backticks."
                    "traduza a resenha para pt br ao passar para o json em todos as iteracoes"
                )
            },
            {"role": "user", "content": pergunta}
        ],
        temperature=0.7,   # reduzir temperatura acelera menos criatividade
        max_tokens=150,    # limite pequeno para respostas curtas
    )
    return resposta.choices[0].message.content

def extrair_json(texto):
    padrao = r"```(?:json)?\s*([\s\S]*?)\s*```"
    match = re.search(padrao, texto)
    return match.group(1).strip() if match else texto.strip()

def iterar_linhas_documento():
    linhas = carregar_arquivo(caminho)
    total = len(linhas)
    resultados = []
    
    for idx, linha in enumerate(linhas, 1):
        print(f"Processando {idx}/{total}...", end=" ", flush=True)
        inicio = time.time()
        
        resposta = ia_lmstudio(linha)
        json_str = extrair_json(resposta)
        try:
            dados = json.loads(json_str)
            resultados.append(dados)
            print(f"OK ({time.time()-inicio:.2f}s)")
        except json.JSONDecodeError as e:
            print(f"ERRO")
            print(f"  Linha: {linha}")
            print(f"  Resposta bruta: {resposta[:200]}...")
            
    
    return resultados

if __name__ == "__main__":
    print("Iniciando processamento...")
    final = iterar_linhas_documento()
    print(f"\nTotal processados: {len(final)}")
    print(json.dumps(final, indent=2, ensure_ascii=False))