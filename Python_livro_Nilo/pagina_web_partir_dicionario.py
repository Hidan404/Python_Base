import os

filmes = {
    "001": {
        "titulo": "O Senhor dos Anéis: A Sociedade do Anel",
        "diretor": "Peter Jackson",
        "ano": 2001,
        "genero": "Fantasia",
    },
    "002": {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "ano": 2010,
        "genero": "Ficção Científica",
    },
    "003": {
        "titulo": "O Poderoso Chefão",
        "diretor": "Francis Ford Coppola",
        "ano": 1972,
        "genero": "Crime",
    },
}

def pasta_arquivo_web():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    pasta_web = os.path.join(diretorio_atual, "web")
    if not os.path.exists(pasta_web):
        os.makedirs(pasta_web)
    return pasta_web

with open(pasta_arquivo_web() + "/filmes.html", "w", encoding="utf-8") as arquivo:
    arquivo.write("<html>\n")
    arquivo.write("<head><title>Lista de Filmes</title></head>\n")
    arquivo.write("<body>\n")
    arquivo.write("<h1>Lista de Filmes</h1>\n")
    arquivo.write("<ul>\n")
    
    for filme_id, detalhes in filmes.items():
        arquivo.write(f"  <li>\n")
        arquivo.write(f"    <strong>{detalhes['titulo']}</strong> ({detalhes['ano']})<br>\n")
        arquivo.write(f"    <p>Diretor: {detalhes['diretor']}</p><br>\n")
        arquivo.write(f"    Gênero: {detalhes['genero']}\n")
        arquivo.write(f"  </li>\n")
    
    arquivo.write("</ul>\n")
    arquivo.write("</body>\n")
    arquivo.write("</html>\n")